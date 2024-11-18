from antlr4 import *
from FOOLILexer import FOOLILexer
from FOOLIParser import FOOLIParser
from GeradorDeCodigo import GeradorDeCodigo

def main():
    # Verifica se o arquivo existe e pode ser aberto
    try:
        input_stream = FileStream("programa.fooli")  # Altere para o nome correto
    except FileNotFoundError:
        print("Arquivo 'programa.fooli' não encontrado!")
        return
    
    lexer = FOOLILexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FOOLIParser(stream)

    # Analisando a árvore sintática a partir da regra 'program'
    print("Iniciando análise...")
    tree = parser.program()

    # Mostra a árvore sintática (para verificar se a análise está ocorrendo corretamente)
    print("Árvore sintática gerada:")
    print(tree.toStringTree(recog=parser))

    # Criando o gerador de código
    gerador = GeradorDeCodigo()
    
    # Visitando a árvore de análise
    print("Gerando código intermediário...")
    gerador.visit(tree)
    print("Código gerado com sucesso!")

if __name__ == '__main__':
    main()
