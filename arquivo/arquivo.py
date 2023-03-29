###▪ Desenvolva um protótipo de software que faça a leitura do arquivo de uma dada instância, 
##mostre um determinado resultado na tela e o salve em um outro arquivo;
##Uma função de entrada deverá ler o conteúdo do arquivo da respectiva instância e armazená-lo 
## em uma matriz do tipo Numpy (consulte a documentação da biblioteca em https://numpy.org);
## ▪ Obtenha a dimensão da matriz (i.e. quantidade de linhas e de colunas);

#Como resultado, uma função de saída deverá mostrar na tela e salvar em arquivo o nome da 
#instância e a dimensão da respectiva matriz no formato: nome_instância qtd_linhas qtd_colunas


## aqui foi criado a matriz, obtido as informações da matriz  e passado o resultado para outro arquivo; 


import numpy as np

def LeiaArquivo(instancia):
    caminho = 'J:\faculdade\algoritmoGrafos\exe01\Instancias' + instancia + '.txt'

    with open(caminho, 'rb') as f:  ## rb para acessar em modo binario 
              
              data = np.genfromtxt(f,dtype="int32")  ## vai ler o arquivo e criar uma matriz
    return data  

 ## funcao que conta quantidade de linhas
def quantidadeLinhas(matriz):
       qtd_linhas = np.size(matriz,0)
       return qtd_linhas

 ## funcao que conta quantidade de coluna
def quantidadeColuna(matriz):
        qtd_coluna =  np.size(matriz,1)
        return qtd_coluna


def Salvaresultado(resultado):
       stringRes =''
       for res in resultado :
        stringRes += str(res) + ' ' #se stringRes for instância de uma classe definida pelo usuário, o comportamento de += pode ser diferente 
        Criararquivo = open('J:\faculdade\algoritmoGrafos\exe01\resultado\resultado.txt', 'a+')## cria o arquivo
        Criararquivo.writelines(stringRes + '\n')## para escrever texto em arquivo pyton
        Criararquivo.close()
       
def Visualizacao(nome_instância,qtd_linhas,qtd_colunas):
         print('NOME DA INSTÂNCIA:', nome_instância, '\n')
         print('Quantidade de linhas:', qtd_linhas, '\n')
         print('Quantidade de colunas', qtd_colunas)
        
     
      
              
              