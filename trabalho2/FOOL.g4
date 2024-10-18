grammar FOOL;

program
    : classDecl* EOF
    ;

classDecl
    : '{' 'class' CLASS_NAME classBody '}'
    ;

classBody
    : fieldDecl* methodDecl*
    ;

fieldDecl
    : dataType VAR_NAME ';'
    ;

methodDecl
    : dataType VAR_NAME '(' params? ')' block
    ;

params
    : param (',' param)*
    ;

param
    : dataType VAR_NAME
    ;

dataType
    : 'int' | 'bool' | 'void' | CLASS_NAME
    ;

block
    : '{' stmt* '}'
    ;

stmt
    : conditionalStmt
    | returnStmt
    | assignStmt
    | exprStmt
    ;

conditionalStmt
    : 'if' '(' expr ')' block ('else' block)?
    ;

returnStmt
    : 'return' expr? ';'
    ;

assignStmt
    : VAR_NAME '=' expr ';'
    ;

exprStmt
    : expr ';'
    ;

expr
    : logicalOrExpr
    ;

logicalOrExpr
    : logicalOrExpr '||' logicalAndExpr
    | logicalAndExpr
    ;

logicalAndExpr
    : logicalAndExpr '&&' equalityExpr
    | equalityExpr
    ;

equalityExpr
    : equalityExpr '==' relationalExpr
    | relationalExpr
    ;

relationalExpr
    : relationalExpr ('<' | '>') additiveExpr
    | additiveExpr
    ;

additiveExpr
    : additiveExpr '+' multiplicativeExpr
    | multiplicativeExpr
    ;

multiplicativeExpr
    : multiplicativeExpr '*' primaryExpr
    | primaryExpr
    ;

primaryExpr
    : '(' expr ')'
    | VAR_NAME
    | INT_LITERAL
    | 'True'
    | 'False'
    ;

VAR_NAME: [a-zA-Z_] [a-zA-Z_0-9]* ;

INT_LITERAL: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;

LINE_COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;