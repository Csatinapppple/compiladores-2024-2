grammar FOOL;

program
    : classDecl* EOF
    ;

classDecl
    : '{' 'class' IDENTIFICADOR classBody '}'
    ;

classBody
    : fieldDecl* methodDecl*
    ;

fieldDecl
    : dataType IDENTIFICADOR ';'
    ;

methodDecl
    : dataType IDENTIFICADOR '(' params? ')' block
    ;

params
    : param (',' param)*
    ;

param
    : dataType IDENTIFICADOR
    ;

dataType
    : 'int' | 'bool' | 'void' | IDENTIFICADOR
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
    : IDENTIFICADOR '=' expr ';'
    ;

exprStmt
    : expr ';'
    ;

expr
    : logicalOrExpr
    ;

logicalOrExpr
    : logicalOrExpr 'or' logicalAndExpr
    | logicalAndExpr
    ;

logicalAndExpr
    : logicalAndExpr 'and' logicalNotExpr
    | logicalNotExpr
    ;

logicalNotExpr
    : logicalNotExpr 'not' equalityExpr
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
    | IDENTIFICADOR
    | DECIMAL
    | 'True'
    | 'False'
    ;

IDENTIFICADOR: [a-zA-Z_] [a-zA-Z_0-9]* ;

DECIMAL: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;

