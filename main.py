
from arquivo import (arquivo as aq)
from Metodos import (caracteristicas as car)



def main(instancia):
    matriz = aq.LeiaArquivo(instancia)
    print(matriz, '\n') # '\n' para inserir linha em branco ao final do comando

    matrizLinha = aq.quantidadeLinhas(matriz)
    matrizColuna = aq.quantidadeColuna(matriz)



    funcao1 = car.verificaAdjacencia(matriz, 0, 1)
    resultado = [instancia, funcao1] 
    aq.salvaResultado(resultado) 

    aq.Visualizacao(instancia,matrizLinha,matrizColuna)
    print('ola mundo')





    



