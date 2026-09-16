#def quicksort(arr): vai ordenar a lista arr usando o algoritmo de ordenação rápida
#(arr,asc): serve para ordenar a lista arr em "ordem ascendente" se asc for True, ou em "ordem descendente" se asc for False
#QUICK SORT é um algoritmo de ordenação eficiente que utiliza a técnica de divisão e conquista.
#...Ele seleciona um elemento como pivô e particiona o array em duas sublistas: elementos menores que o pivô e elementos maiores que o pivô.
#...Em seguida, ele recursivamente aplica o mesmo processo às sublistas.

# A ideia principal do Quicksort é:

#Escolher um elemento como pivô, separar os outros elementos entre os menores e os maiores que ele, ordenar essas duas partes e juntá-las.
#O "arr" é o parâmetro da função. Ele representa a lista que queremos ordenar.

#CODIGO EXPLICAÇÃO ABAIXO: PASSO A PASSO
#def quicksort(arr):  #O "arr" é o parâmetro da função. Ele representa a lista que queremos ordenar.
 # if len(arr) < 2:  #len() retorna a quantidade de elementos da lista. Ex: len([10, 5, 2, 3])
  #  return arr  # se tem 1o,2,4: vai retornar a quantidade de 3 elemntos ao todo. # n queremos comparar o pivo consigo msm linha 16
  #else:
   # pivo = arr[0]   #Aqui pegamos o primeiro elemento da lista e colocamos na variável pivo.
    #menores = [i for i in arr[1:] if i <= pivo]
    #maiores = [i for i in arr[1:] if i > pivo]
    #return quicksort(menores) + [pivo] + quicksort(maiores) #"Ordene os menores, coloque o pivô no meio e depois
    #... coloque os maiores ordenados."

#print(quicksort([10, 5, 2, 3]))
#[2, 3, 5, 10]

#LEN serve verificar se um texto ou entrada do usuário tem o tamanho correto e quantidade de caracteres esperados.
#... Ex: len("Olá") = 3, len("Olá, mundo!") = 12  
#pyhton .\script.py, para executar o script.py e ver o resultado da ordenação.
#return arr...
#...É como dizer:"A função terminou. Devolva esse resultado."


#quicksort chama ela mesma!
#*Ela vai fazer novamente todo o processo:
#*verificar se a lista tem menos de 2 elementos;
#*escolher um pivô;
#*separar menores;
#*separar maiores;
#*ordenar recursivamente;
#*juntar tudo.



def quicksort(arr, asc=True):
    if len(arr) < 2:  
        return arr 
    else:
        pivo = arr[0]
    if asc:
            menores = [i for i in arr[1:] if i <= pivo]
            maiores = [i for i in arr[1:] if i > pivo]
    else:
            menores = [i for i in arr[1:] if i >= pivo]
            maiores = [i for i in arr[1:] if i < pivo]
    return quicksort(menores, asc) + [pivo] + quicksort(maiores, asc)

print(quicksort([10, 5, 2, 3], asc=True))  # Ordena em ordem ascendente/crescente
print(quicksort([10, 5, 2, 3], asc=False))  # Ordena em ordem descendente/descrescente




#SOBRE API: e um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na web.

import requests #significa que estamos importando a biblioteca requests, que é usada para fazer requisições HTTP em Python.
                #Com ela, podemos enviar solicitações para servidores web e receber respostas.

# Função que fará requisição à API
def consulta_cep(cep): # A função consulta_cep recebe um parâmetro cep, que é o código postal que queremos consultar.
  url = f"https://viacep.com.br/ws/{cep}/json/" # Aqui, estamos criando uma URL para fazer a requisição à API. A URL é formatada com o
                                                #código postal (cep) que queremos consultar.  

  res = requests.get(url) # Aqui, estamos usando a função requests.get() para enviar uma 
                          #solicitação HTTP GET para a URL que criamos. A resposta da API será armazenada na variável res.
  res = res.json() # Aqui, estamos chamando o método .json() na resposta da API. 
                   #Isso converte a resposta em um objeto Python (geralmente um dicionário)
  return (res['logradouro'], res['uf']) # Aqui, estamos retornando uma tupla contendo o logradouro (rua) e a 
                                        #unidade federativa (estado) do código postal consultado.

# Lista de CEPs para consulta
lista_cep = ["13186642",  # SIGNIFICA QUE É UMA LISTA DE CEPs (Códigos de Endereçamento Postal) QUE SERÃO CONSULTADOS NA API.
             "13178574",  # SIGNIFICA QUE CADA CEP É UM ELEMENTO DA LISTA, E CADA ELEMENTO É UMA STRING (TEXTO) QUE REPRESENTA UM CEP.
             "13188020",  #SIGNIFICA QUE A LISTA PODE SER USADA PARA FAZER CONSULTAS EM MASSA, OU SEJA, VÁRIOS CEPs DE UMA VEZ.
             "13184321",  #SIGNIFICA QUE A LISTA PODE SER USADA PARA FAZER CONSULTAS EM MASSA, OU SEJA, VÁRIOS CEPs DE UMA VEZ.
             "20720293"]  # SIGNIFICA QUE A LISTA PODE SER USADA PARA FAZER CONSULTAS EM MASSA, OU SEJA, VÁRIOS CEPs DE UMA VEZ.

[consulta_cep(cep)[0] for cep in lista_cep if consulta_cep(cep)[1] == "SP"] # SIGNIFICA QUE ESTAMOS USANDO UMA LIST COMPREHENSION 
                                                                        #PARA CRIAR UMA NOVA LISTA.    