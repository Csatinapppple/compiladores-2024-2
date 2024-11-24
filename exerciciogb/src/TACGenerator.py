class TACGenerator:
    def __init__(self):
        self.temp_counter = 0  # Counter for generating temporary variables
        self.label_counter = 0  # Counter for generating labels
        self.code = []  # List to store TAC instructions

    def new_temp(self):
        """Generate a new temporary variable."""
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def new_label(self):
        """Generate a new label."""
        self.label_counter += 1
        return f"L{self.label_counter}"

    def generate_expr(self, expr_ctx):
        """
        Generate TAC for an expression.
        This is a placeholder for now and will depend on the specific context of the expression rule.
        """
        if expr_ctx is None:
            return None

        # Simplified logic for expressions (example)
        if len(expr_ctx.children) == 3:  # Binary expression, e.g., a + b
            left = expr_ctx.children[0].getText()
            op = expr_ctx.children[1].getText()
            right = expr_ctx.children[2].getText()
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {op} {right}")
            return temp

        elif len(expr_ctx.children) == 1:  # Single variable or literal
            return expr_ctx.getText()

    def generate_assignment(self, assign_ctx):
        """
        Generate TAC for an assignment statement.
        """
        variable = assign_ctx.IDENTIFICADOR().getText()
        expr_temp = self.generate_expr(assign_ctx.expr())
        self.code.append(f"{variable} = {expr_temp}")

    def generate_conditional(self, cond_ctx):
        """
        Generate TAC for if-else or while constructs.
        """
        # Example for 'if' without 'else'
        condition_temp = self.generate_expr(cond_ctx.expr())
        false_label = self.new_label()
        self.code.append(f"if {condition_temp} == 0 goto {false_label}")
        
        # Body of the 'if' block (placeholder logic)
        self.code.append(f"# Code for 'if' body")
        
        self.code.append(f"{false_label}:")

    def generate_while(self, while_ctx):
        """
        Generate TAC for a while loop.
        """
        start_label = self.new_label()
        end_label = self.new_label()

        self.code.append(f"{start_label}:")
        condition_temp = self.generate_expr(while_ctx.expr())
        self.code.append(f"if {condition_temp} == 0 goto {end_label}")
        
        # Body of the 'while' loop (placeholder logic)
        self.code.append(f"# Code for 'while' body")
        
        self.code.append(f"goto {start_label}")
        self.code.append(f"{end_label}:")

    def generate(self, ctx):
        """
        Top-level function to generate TAC for a parse tree context.
        """
        # Placeholder: Iterate over child nodes and process based on their type
        for child in ctx.children:
            if hasattr(child, 'expr'):  # Example for expression nodes
                self.generate_expr(child.expr)
            elif hasattr(child, 'stmt'):  # Example for statement nodes
                self.generate_assignment(child.stmt)

