from FOOLIListener import FOOLIListener
from FOOLIParser import FOOLIParser
from TabelaDeSimbolos import TabelaDeSimbolos

class AnalisadorSemantico(FOOLIListener):
    def __init__(self):
        self.tabela = TabelaDeSimbolos()

    def enterFieldDecl(self, ctx):
        tipo = ctx.dataType().getText()
        nome = ctx.IDENTIFICADOR().getText()
        print(f"Declarando variável: {nome} do tipo {tipo}")
        self.tabela.adicionar(nome, tipo)

    def enterAssign(self, ctx):
        nome = ctx.IDENTIFICADOR().getText()
        expr = ctx.expr().getText()

        # Verifica se a variável foi declarada
        if not self.tabela.buscar(nome):
            raise Exception(f"Erro: variável {nome} não declarada.")

        print(f"Atribuindo: {nome} = {expr}")

    def enterMethodDecl(self, ctx):
        tipo = ctx.dataType().getText()
        nome = ctx.IDENTIFICADOR().getText()
        print(f"Declarando método: {nome} do tipo {tipo}")

    def enterWhileStmt(self, ctx):
        print("Entrando no comando while")
