from FOOLIParser import FOOLIParser

class FOOLIVisitor:
    def visitAssign(self, ctx:FOOLIParser.AssignContext):
        raise NotImplementedError()

    def visitExpr(self, ctx:FOOLIParser.ExprContext):
        raise NotImplementedError()

    def visitWhileStmt(self, ctx:FOOLIParser.WhileStmtContext):
        raise NotImplementedError()

    def visitBlock(self, ctx:FOOLIParser.BlockContext):
        raise NotImplementedError()
