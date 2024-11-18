from FOOLIParser import FOOLIParser
from FOOLILexer import FOOLILexer

class GeradorDeCodigo:
    def __init__(self):
        self.contador_temp = 0

    def gerar_temp(self):
        temp = f"T{self.contador_temp}"
        self.contador_temp += 1
        return temp

    def gerar_codigo(self, comando):
        print(comando)

    def visitAssign(self, ctx:FOOLIParser.AssignContext):
        var = ctx.IDENTIFICADOR().getText()
        expr = self.visit(ctx.expr())  # Vamos gerar o código para a expressão
        temp = self.gerar_temp()
        self.gerar_codigo(f"{temp} = {expr}")
        self.gerar_codigo(f"{var} = {temp}")

    def visitExpr(self, ctx:FOOLIParser.ExprContext):
        # Lidar com expressões. Você pode implementar isso dependendo da complexidade da sua gramática.
        if ctx.getChildCount() == 1:
            return ctx.getText()
        else:
            # Caso de uma expressão mais complexa, como `x + 1`, você pode usar um visitor recursivo para calcular.
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            temp = self.gerar_temp()
            self.gerar_codigo(f"{temp} = {left} {op} {right}")
            return temp

    def visitWhileStmt(self, ctx:FOOLIParser.WhileStmtContext):
        # Geração de código para o comando while
        expr = self.visit(ctx.expr())
        block = self.visit(ctx.block())
        self.gerar_codigo(f"while ({expr}) {block}")

    def visitBlock(self, ctx:FOOLIParser.BlockContext):
        # Geração de código para o bloco
        return "{" + "".join([self.visit(stmt) for stmt in ctx.stmt()]) + "}"

    def visit(self, ctx):
        # Método genérico para percorrer a árvore
        if isinstance(ctx, FOOLIParser.AssignContext):
            return self.visitAssign(ctx)
        elif isinstance(ctx, FOOLIParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, FOOLIParser.WhileStmtContext):
            return self.visitWhileStmt(ctx)
        elif isinstance(ctx, FOOLIParser.BlockContext):
            return self.visitBlock(ctx)
        # Adicione mais verificações conforme necessário para outras regras
        return None
