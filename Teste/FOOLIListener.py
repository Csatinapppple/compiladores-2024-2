# Generated from FOOLI.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FOOLIParser import FOOLIParser
else:
    from FOOLIParser import FOOLIParser

# This class defines a complete listener for a parse tree produced by FOOLIParser.
class FOOLIListener(ParseTreeListener):

    # Enter a parse tree produced by FOOLIParser#program.
    def enterProgram(self, ctx:FOOLIParser.ProgramContext):
        pass

    # Exit a parse tree produced by FOOLIParser#program.
    def exitProgram(self, ctx:FOOLIParser.ProgramContext):
        pass


    # Enter a parse tree produced by FOOLIParser#classDecl.
    def enterClassDecl(self, ctx:FOOLIParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by FOOLIParser#classDecl.
    def exitClassDecl(self, ctx:FOOLIParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by FOOLIParser#classBody.
    def enterClassBody(self, ctx:FOOLIParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by FOOLIParser#classBody.
    def exitClassBody(self, ctx:FOOLIParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by FOOLIParser#fieldDecl.
    def enterFieldDecl(self, ctx:FOOLIParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by FOOLIParser#fieldDecl.
    def exitFieldDecl(self, ctx:FOOLIParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by FOOLIParser#methodDecl.
    def enterMethodDecl(self, ctx:FOOLIParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by FOOLIParser#methodDecl.
    def exitMethodDecl(self, ctx:FOOLIParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by FOOLIParser#params.
    def enterParams(self, ctx:FOOLIParser.ParamsContext):
        pass

    # Exit a parse tree produced by FOOLIParser#params.
    def exitParams(self, ctx:FOOLIParser.ParamsContext):
        pass


    # Enter a parse tree produced by FOOLIParser#param.
    def enterParam(self, ctx:FOOLIParser.ParamContext):
        pass

    # Exit a parse tree produced by FOOLIParser#param.
    def exitParam(self, ctx:FOOLIParser.ParamContext):
        pass


    # Enter a parse tree produced by FOOLIParser#dataType.
    def enterDataType(self, ctx:FOOLIParser.DataTypeContext):
        pass

    # Exit a parse tree produced by FOOLIParser#dataType.
    def exitDataType(self, ctx:FOOLIParser.DataTypeContext):
        pass


    # Enter a parse tree produced by FOOLIParser#block.
    def enterBlock(self, ctx:FOOLIParser.BlockContext):
        pass

    # Exit a parse tree produced by FOOLIParser#block.
    def exitBlock(self, ctx:FOOLIParser.BlockContext):
        pass


    # Enter a parse tree produced by FOOLIParser#stmt.
    def enterStmt(self, ctx:FOOLIParser.StmtContext):
        pass

    # Exit a parse tree produced by FOOLIParser#stmt.
    def exitStmt(self, ctx:FOOLIParser.StmtContext):
        pass


    # Enter a parse tree produced by FOOLIParser#whileStmt.
    def enterWhileStmt(self, ctx:FOOLIParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by FOOLIParser#whileStmt.
    def exitWhileStmt(self, ctx:FOOLIParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by FOOLIParser#conditional.
    def enterConditional(self, ctx:FOOLIParser.ConditionalContext):
        pass

    # Exit a parse tree produced by FOOLIParser#conditional.
    def exitConditional(self, ctx:FOOLIParser.ConditionalContext):
        pass


    # Enter a parse tree produced by FOOLIParser#returnStmt.
    def enterReturnStmt(self, ctx:FOOLIParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by FOOLIParser#returnStmt.
    def exitReturnStmt(self, ctx:FOOLIParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by FOOLIParser#assign.
    def enterAssign(self, ctx:FOOLIParser.AssignContext):
        pass

    # Exit a parse tree produced by FOOLIParser#assign.
    def exitAssign(self, ctx:FOOLIParser.AssignContext):
        pass


    # Enter a parse tree produced by FOOLIParser#expr.
    def enterExpr(self, ctx:FOOLIParser.ExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#expr.
    def exitExpr(self, ctx:FOOLIParser.ExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:FOOLIParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:FOOLIParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:FOOLIParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:FOOLIParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#equalityExpr.
    def enterEqualityExpr(self, ctx:FOOLIParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#equalityExpr.
    def exitEqualityExpr(self, ctx:FOOLIParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#relationalExpr.
    def enterRelationalExpr(self, ctx:FOOLIParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#relationalExpr.
    def exitRelationalExpr(self, ctx:FOOLIParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:FOOLIParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:FOOLIParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:FOOLIParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:FOOLIParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:FOOLIParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by FOOLIParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:FOOLIParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by FOOLIParser#methodCall.
    def enterMethodCall(self, ctx:FOOLIParser.MethodCallContext):
        pass

    # Exit a parse tree produced by FOOLIParser#methodCall.
    def exitMethodCall(self, ctx:FOOLIParser.MethodCallContext):
        pass


    # Enter a parse tree produced by FOOLIParser#arguments.
    def enterArguments(self, ctx:FOOLIParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by FOOLIParser#arguments.
    def exitArguments(self, ctx:FOOLIParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by FOOLIParser#argument.
    def enterArgument(self, ctx:FOOLIParser.ArgumentContext):
        pass

    # Exit a parse tree produced by FOOLIParser#argument.
    def exitArgument(self, ctx:FOOLIParser.ArgumentContext):
        pass


