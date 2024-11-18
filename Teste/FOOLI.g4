grammar FOOLI;

program
    : classDecl* EOF?
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
    | 'void' 'main' '(' ')' block
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
    : conditional
    | returnStmt ';'
    | assign ';'
    | expr ';'
    | whileStmt
    ;

whileStmt
    : 'while' '(' expr ')' block
    ;

conditional
    : 'if' '(' expr ')' block ('else' block)?
    ;

returnStmt
    : 'return' expr?
    ;

assign
    : IDENTIFICADOR '=' expr
    ;

expr
    : logicalOrExpr
    ;

logicalOrExpr
    : logicalOrExpr 'or' logicalAndExpr
    | logicalAndExpr
    ;

logicalAndExpr
    : logicalAndExpr 'and' equalityExpr
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
    | methodCall
    | 'True'
    | 'False'
    | 'not' primaryExpr
    ;

methodCall
    : IDENTIFICADOR '(' arguments? ')'
    ;

arguments
    : argument (',' argument)*
    ;

argument
    : expr
    ;

IDENTIFICADOR: [a-zA-Z_] [a-zA-Z_0-9]* ;

DECIMAL: [0-9]+ ;

WHITESPACE: [ \t\r\n]+ -> skip ;
