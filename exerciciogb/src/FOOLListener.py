# Generated from FOOL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FOOLParser import FOOLParser
else:
    from FOOLParser import FOOLParser

# This class defines a complete listener for a parse tree produced by FOOLParser.
class FOOLListener(ParseTreeListener):

    # Enter a parse tree produced by FOOLParser#program.
    def enterProgram(self, ctx:FOOLParser.ProgramContext):
        pass

    # Exit a parse tree produced by FOOLParser#program.
    def exitProgram(self, ctx:FOOLParser.ProgramContext):
        pass


    # Enter a parse tree produced by FOOLParser#classDecl.
    def enterClassDecl(self, ctx:FOOLParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by FOOLParser#classDecl.
    def exitClassDecl(self, ctx:FOOLParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by FOOLParser#classBody.
    def enterClassBody(self, ctx:FOOLParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by FOOLParser#classBody.
    def exitClassBody(self, ctx:FOOLParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by FOOLParser#fieldDecl.
    def enterFieldDecl(self, ctx:FOOLParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by FOOLParser#fieldDecl.
    def exitFieldDecl(self, ctx:FOOLParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by FOOLParser#mainDecl.
    def enterMainDecl(self, ctx:FOOLParser.MainDeclContext):
        pass

    # Exit a parse tree produced by FOOLParser#mainDecl.
    def exitMainDecl(self, ctx:FOOLParser.MainDeclContext):
        pass


    # Enter a parse tree produced by FOOLParser#methodDecl.
    def enterMethodDecl(self, ctx:FOOLParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by FOOLParser#methodDecl.
    def exitMethodDecl(self, ctx:FOOLParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by FOOLParser#params.
    def enterParams(self, ctx:FOOLParser.ParamsContext):
        pass

    # Exit a parse tree produced by FOOLParser#params.
    def exitParams(self, ctx:FOOLParser.ParamsContext):
        pass


    # Enter a parse tree produced by FOOLParser#param.
    def enterParam(self, ctx:FOOLParser.ParamContext):
        pass

    # Exit a parse tree produced by FOOLParser#param.
    def exitParam(self, ctx:FOOLParser.ParamContext):
        pass


    # Enter a parse tree produced by FOOLParser#dataType.
    def enterDataType(self, ctx:FOOLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by FOOLParser#dataType.
    def exitDataType(self, ctx:FOOLParser.DataTypeContext):
        pass


    # Enter a parse tree produced by FOOLParser#block.
    def enterBlock(self, ctx:FOOLParser.BlockContext):
        pass

    # Exit a parse tree produced by FOOLParser#block.
    def exitBlock(self, ctx:FOOLParser.BlockContext):
        pass


    # Enter a parse tree produced by FOOLParser#stmt.
    def enterStmt(self, ctx:FOOLParser.StmtContext):
        pass

    # Exit a parse tree produced by FOOLParser#stmt.
    def exitStmt(self, ctx:FOOLParser.StmtContext):
        pass


    # Enter a parse tree produced by FOOLParser#conditional.
    def enterConditional(self, ctx:FOOLParser.ConditionalContext):
        pass

    # Exit a parse tree produced by FOOLParser#conditional.
    def exitConditional(self, ctx:FOOLParser.ConditionalContext):
        pass


    # Enter a parse tree produced by FOOLParser#return.
    def enterReturn(self, ctx:FOOLParser.ReturnContext):
        pass

    # Exit a parse tree produced by FOOLParser#return.
    def exitReturn(self, ctx:FOOLParser.ReturnContext):
        pass


    # Enter a parse tree produced by FOOLParser#assign.
    def enterAssign(self, ctx:FOOLParser.AssignContext):
        pass

    # Exit a parse tree produced by FOOLParser#assign.
    def exitAssign(self, ctx:FOOLParser.AssignContext):
        pass


    # Enter a parse tree produced by FOOLParser#expr.
    def enterExpr(self, ctx:FOOLParser.ExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#expr.
    def exitExpr(self, ctx:FOOLParser.ExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#methodCall.
    def enterMethodCall(self, ctx:FOOLParser.MethodCallContext):
        pass

    # Exit a parse tree produced by FOOLParser#methodCall.
    def exitMethodCall(self, ctx:FOOLParser.MethodCallContext):
        pass


    # Enter a parse tree produced by FOOLParser#arguments.
    def enterArguments(self, ctx:FOOLParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by FOOLParser#arguments.
    def exitArguments(self, ctx:FOOLParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by FOOLParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:FOOLParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:FOOLParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:FOOLParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:FOOLParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#equalityExpr.
    def enterEqualityExpr(self, ctx:FOOLParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#equalityExpr.
    def exitEqualityExpr(self, ctx:FOOLParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#relationalExpr.
    def enterRelationalExpr(self, ctx:FOOLParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#relationalExpr.
    def exitRelationalExpr(self, ctx:FOOLParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:FOOLParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:FOOLParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:FOOLParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:FOOLParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by FOOLParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:FOOLParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by FOOLParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:FOOLParser.PrimaryExprContext):
        pass



del FOOLParser