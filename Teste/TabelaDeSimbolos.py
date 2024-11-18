class TabelaDeSimbolos:
    def __init__(self):
        self.tabela = {}

    def adicionar(self, nome, tipo):
        if nome in self.tabela:
            raise Exception(f"Erro: variável {nome} já declarada.")
        self.tabela[nome] = tipo

    def buscar(self, nome):
        return self.tabela.get(nome, None)

    def __str__(self):
        return "\n".join([f"{nome}: {tipo}" for nome, tipo in self.tabela.items()])
