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
    : conditional 
    | return ';'
    | assign ';'
    | expr ';'
    ;

conditional
    : 'if' '(' expr ')' block ('else' block)?
		| 'while' '(' expr ')' block
    ;

return
    : 'return' expr? 
    ;

assign
    : IDENTIFICADOR '=' expr 
    ;

expr
    : logicalOrExpr
    ;

methodCall
	: IDENTIFICADOR '(' arguments? ')'
	;

arguments
	: expr (',' expr)* 
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

IDENTIFICADOR: [a-zA-Z_] [a-zA-Z_0-9]* ;

DECIMAL: [0-9]+ ;

WHITESPACE: [ \t\r\n]+ -> skip ;


