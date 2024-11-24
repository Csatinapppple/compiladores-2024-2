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
        self.code.append(f"{temp} = call {method_name}, {', '.join(args)}")
        return temp

    def process_expression(self, ctx):
        """Handle expressions and generate TAC."""
        if ctx.DECIMAL():
            return ctx.DECIMAL().getText()
        elif ctx.IDENTIFICADOR():
            return ctx.IDENTIFICADOR().getText()
        elif ctx.methodCall():
            return self.enterMethodCall(ctx.methodCall())
        elif len(ctx.children) == 3:  # Binary expressions
            left = self.process_expression(ctx.children[0])
            operator = ctx.children[1].getText()
            right = self.process_expression(ctx.children[2])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {operator} {right}")
            return temp
        elif len(ctx.children) == 2 and ctx.children[0].getText() == "not":  # Unary expressions
            operand = self.process_expression(ctx.children[1])
            temp = self.new_temp()
            self.code.append(f"{temp} = not {operand}")
            return temp
        return ""

