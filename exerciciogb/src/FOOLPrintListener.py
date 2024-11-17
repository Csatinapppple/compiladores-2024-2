from FOOLListener import FOOLListener as Listener
from FOOLParser import FOOLParser as Parser

class FOOLPrintListener(Listener):
    def enterExpr(self, ctx: Parser.ExprContext):
        print(f"Entering Expression: {ctx.getText()}")

    def exitExpr(self, ctx: Parser.ExprContext):
        print(f"Exiting expression: {ctx.getText()}")
