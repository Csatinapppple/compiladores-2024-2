from antlr4 import *
from src.FOOLLexer import FOOLLexer as Lexer
from src.FOOLParser import FOOLParser as Parser

from src.FOOLPrintListener import FOOLPrintListener as PrintListener


file = open("input.txt", "r")
content = file.read()
file.close()

input_stream = FileStream("input.txt");
lexer = Lexer(input_stream)
stream = CommonTokenStream(lexer)
parser = Parser(stream)
tree = parser.expr()


# Walk the tree with the listener
listener = PrintListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
