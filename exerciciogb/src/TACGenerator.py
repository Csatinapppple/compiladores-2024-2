from antlr4 import ParseTreeWalker
from .FOOLListener import FOOLListener as Listener
from .FOOLParser import FOOLParser as Parser

class TACGenerator:
    def __init__(self):
        self.code = []
        self.temp_counter = 0
        self.label_counter = 0

    def new_temp(self):
        """Generate a new temporary variable."""
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def new_label(self):
        """Generate a new label."""
        self.label_counter += 1
        return f"L{self.label_counter}"

    def enterEveryRule(self, ctx):
        """Called when entering any rule."""
        pass

    def exitEveryRule(self, ctx):
        """Called when exiting any rule."""
        pass

    def visitTerminal(self, node):
        """Called when visiting a terminal node."""
        pass

    def visitErrorNode(self, node):
        """Called when visiting an error node."""
        pass

    def enterFieldDecl(self, ctx):
        """Handle field declarations."""
        field_name = ctx.IDENTIFICADOR().getText()
        self.code.append(f"# Field Declaration: {field_name}")

    def enterMainDecl(self, ctx):
        """Handle the main method declaration."""
        self.code.append("main:")

    def exitMainDecl(self, ctx):
        """Handle the end of the main method."""
        self.code.append("End main:")

    def enterAssign(self, ctx):
        """Handle assignment statements."""
        var_name = ctx.IDENTIFICADOR().getText()
        expr_result = self.process_expression(ctx.expr())
        self.code.append(f"{var_name} = {expr_result}")


    def enterConditional(self, ctx):
        """Handle conditionals, including 'if' and 'while'."""
        if ctx.children[0].getText() == 'while':
            # Start and end labels for the loop
            start_label = self.new_label()
            end_label = self.new_label()

            # Add the start label
            self.code.append(f"{start_label}:")

            # Process the condition expression for the while loop
            condition = self.process_expression(ctx.expr())
            self.code.append(f"if {condition} == 0 goto {end_label}")  # Jump if condition is false

            # Process the block of the loop
            block = ctx.block()
            for stmt in block:  # Iterate over each statement in the block
                ParseTreeWalker.DEFAULT.walk(self, stmt)  # Walk through each statement

            # Jump back to the start of the loop
            self.code.append(f"goto {start_label}")
            self.code.append(f"{end_label}:")  # Add the end label


    def enterMethodCall(self, ctx):
        """Handle method calls."""
        method_name = ctx.IDENTIFICADOR().getText()
        args = [self.process_expression(arg) for arg in ctx.arguments().expr()] if ctx.arguments() else []

        temp = self.new_temp()
        if not args:
            self.code.append(f"{temp} = call {method_name}")
        else:
            self.code.append(f"{temp} = call {method_name}, {', '.join(args)}")
        return temp

    def process_expression(self, ctx):
        # Handling Primary Expressions (e.g., literals or identifiers)
        if isinstance(ctx, Parser.PrimaryExprContext):
            if ctx.DECIMAL():
                return ctx.DECIMAL().getText()
            elif ctx.IDENTIFICADOR():
                return ctx.IDENTIFICADOR().getText()
            elif ctx.methodCall():
                return self.enterMethodCall(ctx.methodCall())
            elif len(ctx.children) == 2 and ctx.children[0].getText() == 'not':  # Unary 'not' expression (e.g., not a)
                operator = ctx.children[0].getText()
                operand = self.process_expression(ctx.children[1])
                temp = self.new_temp()
                self.code.append(f"{temp} = {operator} {operand}")
                return temp

        # Handling Additive Expressions (e.g., a + b)
        elif isinstance(ctx, Parser.AdditiveExprContext):
            if len(ctx.children) == 3:  # Binary addition (e.g., a + b)
                left = self.process_expression(ctx.children[0])  # Left operand
                operator = ctx.children[1].getText()  # Additive operator (+)
                right = self.process_expression(ctx.children[2])  # Right operand
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (delegate to next expression rule)
                return self.process_expression(ctx.children[0])

        # Handling Multiplicative Expressions (e.g., a * b)
        elif isinstance(ctx, Parser.MultiplicativeExprContext):
            if len(ctx.children) == 3:  # Binary multiplication (e.g., a * b)
                left = self.process_expression(ctx.children[0])  # Left operand
                operator = ctx.children[1].getText()  # Multiplicative operator (*)
                right = self.process_expression(ctx.children[2])  # Right operand
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (delegate to next expression rule)
                return self.process_expression(ctx.children[0])

        # Handling Equality Expressions (e.g., a == b)
        elif isinstance(ctx, Parser.EqualityExprContext):
            if len(ctx.children) == 3:  # Binary equality (e.g., a == b)
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()  # '==' or '!='
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (e.g., for nested expressions)
                return self.process_expression(ctx.children[0])

        # Handling Relational Expressions (e.g., a < b)
        elif isinstance(ctx, Parser.RelationalExprContext):
            if len(ctx.children) == 3:  # Binary relational expressions (e.g., a < b)
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()  # Relational operator (<, >, <=, >=)
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (e.g., for nested expressions)
                return self.process_expression(ctx.children[0])

        # Handling Logical OR Expressions (e.g., a or b)
        elif isinstance(ctx, Parser.LogicalOrExprContext):
            if len(ctx.children) == 3:  # Binary OR (e.g., a or b)
                left = self.process_expression(ctx.children[0])
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} or {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (delegate to LogicalAndExpr)
                return self.process_expression(ctx.children[0])

        # Handling Logical AND Expressions (e.g., a and b)
        elif isinstance(ctx, Parser.LogicalAndExprContext):
            if len(ctx.children) == 3:  # Binary AND (e.g., a and b)
                left = self.process_expression(ctx.children[0])
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} and {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child case (delegate to next rule)
                return self.process_expression(ctx.children[0])

        # Handling Top-level expr rule (e.g., combination of all above)
        elif isinstance(ctx, Parser.ExprContext):
            if ctx.children:
                return self.process_expression(ctx.children[0])

        else:
            # Debugging information for unexpected contexts
            print(f"Unhandled context in process_expression: {type(ctx)} with children {ctx.children if ctx.children else 'None'}")
            raise NotImplementedError(f"Unhandled expression context: {type(ctx)}")


    def get_code(self):
        """Return the generated code."""
        return "\n".join(self.code)

