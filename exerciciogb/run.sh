antlr4-parse FOOL.g4 program -tree -tokens -trace -gui input.txt | tee output.txt

antlr4 -Dlanguage=Python3 FOOL.g4 # gerar Lexer e Parser da linguagem
