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
        self.code.append(f"# Field Declaration: {ctx.dataType().getText()} {field_name}")

    def enterMainDecl(self, ctx):
        """Handle the main method declaration."""
        self.code.append("main:")
        self.handleBlock(ctx.block())


    def exitMainDecl(self, ctx):
        """Handle the end of the main method."""
        self.code.append("End main:")
    
    def enterMethodDecl(self, ctx):
        """Handle the method declaration."""
        self.code.append(f"{ctx.IDENTIFICADOR().getText()}:")
        self.handleBlock(ctx.block())


    def exitMethodDecl(self, ctx):
        """Handle the end of the method."""
        self.code.append(f"End {ctx.IDENTIFICADOR().getText()}:")

    def handleBlock(self, ctx):
        for child in ctx.getChildren():
            if child.getText() != "{" and child.getText() != "}":
                self.process_stmt(child.children[0])

    def process_stmt(self, ctx):
        """Handle the statements in the grammar."""

        # Handle assignment statements (e.g., x = expr)
        if isinstance(ctx, Parser.AssignContext):
            self.handleAssign(ctx)

        # Handle conditional statements (e.g., if or while)
        elif isinstance(ctx, Parser.ConditionalContext):
            self.handleConditional(ctx)
        # Handle return statements (e.g., return expr)
        elif isinstance(ctx, Parser.ReturnContext):
            self.handleReturn(ctx)

        # Handle method calls (e.g., myMethod())
        elif isinstance(ctx, Parser.MethodCallContext):
            self.handleMethodCall(ctx)
        
        else:
            print(ctx.getText())
            print(f"Unhandled statement context: {type(ctx)}")


    def handleAssign(self, ctx):
        """Handle assignment statements."""
        var_name = ctx.IDENTIFICADOR().getText()
        expr_result = self.process_expression(ctx.expr())
        self.code.append(f"{var_name} = {expr_result}")
    
    def handleReturn(self, ctx):
        """Handle return statements."""
        return_value = self.process_expression(ctx.expr()) if ctx.expr() else "None"
        self.code.append(f"return {return_value}")

    def handleConditional(self, ctx):
        """Handle conditionals, including 'if' and 'while'."""
        if ctx.children[0].getText() == 'while':
            start_label = self.new_label()
            end_label = self.new_label()
            self.code.append(f"{start_label}:")
            condition = self.process_expression(ctx.expr())
            self.code.append(f"if {condition} == False goto {end_label}")
            self.handleBlock(ctx.block(0))
            self.code.append(f"goto {start_label}")
            self.code.append(f"{end_label}:")
        elif ctx.children[0].getText() == 'if':
            condition = self.process_expression(ctx.expr())
            else_label = self.new_label()
            end_label = self.new_label()
            self.code.append(f"if {condition} == False goto {else_label}")
            self.handleBlock(ctx.block(0))
            self.code.append(f"goto {end_label}")
            self.code.append(f"{else_label}:")
            if len(ctx.block()) > 1:
                self.handleBlock(ctx.block(1))
            self.code.append(f"{end_label}:")


    def handleMethodCall(self, ctx):
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
                return self.handleMethodCall(ctx.methodCall())
            elif len(ctx.children) == 2 and ctx.children[0].getText() == 'not':  # Unary 'not' expression (e.g., not a)
                operator = ctx.children[0].getText()
                operand = self.process_expression(ctx.children[1])
                temp = self.new_temp()
                self.code.append(f"{temp} = {operator} {operand}")
                return temp
            elif ctx.children[0].getText() == '(' and ctx.children[-1].getText() == ')':  # Parenthesized expression
                return self.process_expression(ctx.children[1])  # Process the inner expression
            elif ctx.children[0].getText() == 'True':  # Boolean literal `True`
                return "True"  # Represent `True` as `1` in TAC
            elif ctx.children[0].getText() == 'False':  # Boolean literal `False`
                return "False"  # Represent `False` as `0` in TAC

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

