from antlr4 import *
from src.FOOLParser import FOOLParser
from src.FOOLListener import FOOLListener

class TACGenerator(FOOLListener):
    def __init__(self):
        self.temp_count = 0  # Counter for temporary variables
        self.code = []  # List to store TAC instructions
        self.symbol_table = {}  # Symbol table for variable tracking
        self.current_scope = "global"  # Current scope (e.g., global, method-specific)

    def new_temp(self):
        """Generates a new temporary variable."""
        self.temp_count += 1
        return f"t{self.temp_count}"

    def enterMainDecl(self, ctx: FOOLParser.MainDeclContext):
        """Handles the entry of the main method."""
        self.code.append("main:")

    def enterAssign(self, ctx: FOOLParser.AssignContext):
        """Handles assignments."""
        variable = ctx.IDENTIFICADOR().getText()
        expr_result = self.process_expression(ctx.expr())
        self.code.append(f"{variable} = {expr_result}")

    def process_expression(self, ctx):
        """Processes expressions and generates TAC."""
        if isinstance(ctx, FOOLParser.PrimaryExprContext):
            # Handle literals, identifiers, or method calls
            if ctx.IDENTIFICADOR():
                return ctx.IDENTIFICADOR().getText()
            elif ctx.DECIMAL():
                return ctx.DECIMAL().getText()
            elif ctx.methodCall():
                return self.process_method_call(ctx.methodCall())
            elif ctx.expr():
                return self.process_expression(ctx.expr())
        elif isinstance(ctx, FOOLParser.AdditiveExprContext):
            # Handle addition
            left = self.process_expression(ctx.additiveExpr(0))
            right = self.process_expression(ctx.additiveExpr(1))
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} + {right}")
            return temp
        elif isinstance(ctx, FOOLParser.MultiplicativeExprContext):
            # Handle multiplication
            left = self.process_expression(ctx.multiplicativeExpr(0))
            right = self.process_expression(ctx.multiplicativeExpr(1))
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} * {right}")
            return temp
        elif isinstance(ctx, FOOLParser.RelationalExprContext):
            # Handle relational expressions
            left = self.process_expression(ctx.relationalExpr(0))
            right = self.process_expression(ctx.relationalExpr(1))
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} < {right}")  # Example for '<'
            return temp
        # Extend for other expressions as needed
        return ""

    def process_method_call(self, ctx):
        """Processes a method call and generates TAC."""
        method_name = ctx.IDENTIFICADOR().getText()
        arguments = [self.process_expression(arg) for arg in ctx.arguments().expr()] if ctx.arguments() else []
        temp = self.new_temp()
        self.code.append(f"{temp} = call {method_name}, {', '.join(arguments)}")
        return temp

    def exitMainDecl(self, ctx: FOOLParser.MainDeclContext):
        """Handles the exit of the main method."""
        self.code.append("end main")

