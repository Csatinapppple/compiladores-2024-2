from antlr4 import *
from src.FOOLLexer import FOOLLexer as Lexer
from src.FOOLParser import FOOLParser as Parser

from src.FOOLPrintListener import FOOLPrintListener as PrintListener


file = open("input.txt", "r")
content = file.read()
file.close()

input_stream = FileStream("input.txt");
print(input_stream)
lexer = Lexer(input_stream)
print(lexer)
stream = CommonTokenStream(lexer)
print(stream)
parser = Parser(stream)
print(parser)
tree = parser.expr()
print(tree)


# Walk the tree with the listener
listener = PrintListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
