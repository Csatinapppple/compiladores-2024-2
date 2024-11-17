from antlr4 import *
from src.FOOLLexer import FOOLLexer as Lexer
from src.FOOLParser import FOOLParser as Parser
from src.FOOLPrintListener import FOOLPrintListener as PrintListener


file = open("input.txt", "r")
content = file.read()
file.close()

input_stream = InputStream(content);
lexer = ArithmeticLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ArithmeticParser(stream)
tree = parser.expr()

# Walk the tree with the listener
listener = ArithmeticPrintListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
