from antlr4 import ParseTreeWalker
from .FOOLListener import FOOLListener as Listener
from .FOOLParser import FOOLParser as Parser


class TACGenerator(Listener):
    def __init__(self):
        self.temp_count = 0  # Counter for temporary variables
        self.label_count = 0  # Counter for labels
        self.code = []  # List to store TAC instructions
        self.symbol_table = {}  # Symbol table to track variables and fields

    def new_temp(self):
        """Generate a new temporary variable."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        """Generate a new label."""
        self.label_count += 1
        return f"L{self.label_count}"

    def enterFieldDecl(self, ctx: Parser.FieldDeclContext):
        """Handle field declarations."""
        field_name = ctx.IDENTIFICADOR().getText()
        print(field_name)
        self.symbol_table[field_name] = "field"
        self.code.append(f"# Field Declaration: {field_name}")

    def enterMainDecl(self, ctx: Parser.MainDeclContext):
        """Handle the start of the main method."""
        self.code.append("main:")

    def exitMainDecl(self, ctx: Parser.MainDeclContext):
        """Handle the end of the main method."""
        self.code.append("End main:")

    def enterAssign(self, ctx: Parser.AssignContext):
        """Handle assignments."""
        variable = ctx.IDENTIFICADOR().getText()
        expr_result = self.process_expression(ctx.expr())
        self.code.append(f"{variable} = {expr_result}")
    
    def enterConditional(self, ctx: Parser.ConditionalContext):
        """Handle conditionals, including 'if' and 'while'."""
        if ctx.children[0].getText() == 'while':
            # Handle the 'while' loop
            start_label = self.new_label()  # Create a start label
            end_label = self.new_label()    # Create an end label

            self.code.append(f"{start_label}:")  # Label for the start of the loop
            
            # Process the condition expression for the while loop
            condition = self.process_expression(ctx.expr())
            self.code.append(f"if {condition} == 0 goto {end_label}")  # Condition check
            
            # Process the body of the loop (block of statements)
            block = ctx.block()
            for stmt in block:  # Iterate over each statement in the block
                ParseTreeWalker.DEFAULT.walk(self, stmt)  # Walk through each statement in the block

            # Generate a jump back to the start of the loop
            self.code.append(f"goto {start_label}")
            self.code.append(f"{end_label}:")  # Label for the end of the loop

    def enterWhileLoop(self, ctx: Parser.ConditionalContext):
        """Handle while loops."""
        start_label = self.new_label()
        end_label = self.new_label()

        self.code.append(f"{start_label}:")
        condition_result = self.process_expression(ctx.expr())
        self.code.append(f"if {condition_result} == 0 goto {end_label}")
        # The loop body will be processed as part of the walker
        self.code.append(f"goto {start_label}")
        self.code.append(f"{end_label}:")

    def enterMethodCall(self, ctx: Parser.MethodCallContext):
        """Handle method calls."""
        method_name = ctx.IDENTIFICADOR().getText()
        args = [self.process_expression(arg) for arg in ctx.arguments().expr()] if ctx.arguments() else []

        temp = self.new_temp()

        if not args:  # No arguments
            self.code.append(f"{temp} = call {method_name}")
        else:  # With arguments
            self.code.append(f"{temp} = call {method_name}, {', '.join(args)}")

        return temp

    def process_expression(self, ctx):
        """Handle expressions and generate TAC."""
        if ctx is None:
            raise ValueError("Received None context in process_expression")

        if isinstance(ctx, Parser.PrimaryExprContext):  # Primary expressions
            if ctx.DECIMAL():
                return ctx.DECIMAL().getText()
            elif ctx.IDENTIFICADOR():
                return ctx.IDENTIFICADOR().getText()
            elif ctx.methodCall():
                return self.enterMethodCall(ctx.methodCall())
            elif len(ctx.children) == 2 and ctx.children[0].getText() == "not":  # Unary 'not'
                operand = self.process_expression(ctx.children[1])
                temp = self.new_temp()
                self.code.append(f"{temp} = not {operand}")
                return temp
        elif isinstance(ctx, Parser.AdditiveExprContext):  # Additive expressions
            if len(ctx.children) >= 3:
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
        elif isinstance(ctx, Parser.MultiplicativeExprContext):  # Multiplicative expressions
            if len(ctx.children) >= 3:
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
        elif isinstance(ctx, Parser.RelationalExprContext):  # Relational expressions
            if len(ctx.children) >= 3:
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
        elif isinstance(ctx, Parser.EqualityExprContext):  # Equality expressions
            if len(ctx.children) >= 3:
                left = self.process_expression(ctx.children[0])
                operator = ctx.children[1].getText()  # Should be '=='
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
        elif isinstance(ctx, Parser.LogicalOrExprContext):  # Logical OR
            if len(ctx.children) == 3:  # Binary OR expression
                left = self.process_expression(ctx.children[0])
                operator = "or"
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child: delegate to logicalAndExpr
                return self.process_expression(ctx.children[0])
        elif isinstance(ctx, Parser.LogicalAndExprContext):  # Logical AND
            if len(ctx.children) == 3:  # Binary AND expression
                left = self.process_expression(ctx.children[0])
                operator = "and"
                right = self.process_expression(ctx.children[2])
                temp = self.new_temp()
                self.code.append(f"{temp} = {left} {operator} {right}")
                return temp
            elif len(ctx.children) == 1:  # Single child: delegate to next rule
                return self.process_expression(ctx.children[0])
        elif isinstance(ctx, Parser.ExprContext):  # Top-level expr rule
            if ctx.children:
                return self.process_expression(ctx.children[0])
        else:
            # Debugging information for unexpected contexts
            print(f"Unhandled context in process_expression: {type(ctx)}, children: {ctx.children if ctx.children else 'None'}")
            raise NotImplementedError(f"Unhandled expression context: {type(ctx)}")

