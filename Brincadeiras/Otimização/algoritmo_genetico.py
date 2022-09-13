'''
Autor: Daniel Paiva Salles
Sintese: Utilizar a técnica de algoritmo genético para trabalhar a otimização de uma situação hipotética.
Problema proposto: Uma empresa de emplacamento de veículos esta precisando realizar a compra de porcas, parafusos e 
arruelas para repor o estoque. Todos os itens são vendidos em pacotes fechados e valores distintos, e todos os itens
possuem suas versões finas e grossas. O valor dos itens finos são: Porcas(R$30,52), Parafusos(R$28,75), 
Soberbos(R$29,63), Arruelas(R$26,74).
Os itens grossos são: Porcas(R$36,13), Parafusos(R$34,19), Soberbos(R$35,48), Arruelas(R$31,32).
A empresa disponibiliza de R$1500 para a aquisição destes insumos. Deve ser adiquirido todos os itens na maior
quantidade possível, respeitando o dinheiro disponível e adiquirindo todos os itens. 
A proporção de compra para porcas/arruelas/parafusos se da pela proporção seguinte proporção:
Porca/Parafuso= 1:1
Parafuso/Soberbo= 1:1
Soberbo/Arruela= 1:1
Parafuso/Arruela= 1:2
'''
from cProfile import label
import random
import pandas as pd

#Etapas:
# -Inicialização: Setar cromossomos aleatórios --CHECK
# -Medir a adaptação --CHECK
# -Elitismo --CHECK
# -Crossover 
# --Roleta --CHECK
# --Ponto de corte
# -Mutação
# -Ir pra proxima geração

#Definições
#Cada gene terá 8 cromossomos; Cada cromossomo pertencerá ao conjunto dos numeros NATURAIS; Os genes serão agrupados
#em duas partes, os quatro primeiros cromossomos pertencerão ao conjunto fino e os quatro ultimos ao conjunto grosso;
#A ordem dos cromossomos será, nos dois grupos, Parafuso(Pa), Porca(Po), Soberbo(So), Arruela(Ar); Cada população 
#proposta como solução terá 7 genes; O mais bem adaptado será mantido por elitismo.
'''
ETAPA 0
-Constantes
-Variaveis
-Metodos
'''
#Constantes
#Valores = preço de cada parafuso
VALORES = pd.Series([15, 14, 15, 14, 18, 17, 16, 16])
#Limite = numero de iterações de evolução
LIMITE = 1000

#O metodo randomizar irá retornar os cromossomos do meu gene
def randomizar():
    return random.randint(1, 15)

#O metodo de adaptabilidade vai retornar os genes mais adaptados por roleta, ponderando o mais e o menos adaptado
def adaptabilidade(adaptacao):
    #atributo adaptacao vai receber o quadrado de si mesmo para retirar valores negativos
    adaptacao = adaptacao**2
    #atributo adaptacao vai ordenar valores do menos apto ao mais apto
    adaptacao = adaptacao.sort_values(by=0, ascending=False)
    #retorno com os dados ordenados e ponderados conforme sua adaptabilidade
    return adaptacao.sample(n = 6, weights=[1, 2, 4, 8, 16, 32])

#O metodo de cruzamento vai pegar dois genes mais bem adaptados para cruzar os cromossomos
def cruzamento(adaptacao):
    teste = adaptabilidade(adaptacao)
    #genes_cruzados = pd.DataFrame([adaptabilidade(adaptacao)], [adaptabilidade(adaptacao)])
    return teste

'''
ETAPA 1
-Criação inicial de cromossomos
'''
cromossomo = []
for x in range(7):
    cromossomo.append([randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar()])

populacao = pd.DataFrame(cromossomo)

'''
ETAPA 2
-Calculo de adaptabilidade dos genes
'''
adaptacao = []
for x in range(7):
    acumulador = 0
    for y in range(8):
        acumulador += populacao.iloc[x, y] * VALORES.iloc[y]
    acumulador -= LIMITE
    adaptacao.append(acumulador)

adaptacao = pd.DataFrame(adaptacao)

'''
ETAPA 3
-Elitismo, separação do melhor gene para a proxima população.
'''
flag = True
for x in range(7):
    if flag:
        acumulador = adaptacao.iloc[x, 0]
        indice = x
        flag = False
    elif(acumulador**2 >= adaptacao.iloc[x, 0]**2):
        acumulador = adaptacao.iloc[x, 0]
        indice = x
nova_populacao = populacao.iloc[[indice]]

'''
Etapa 4
-Crossover, cruzamento de cromossomos para a geração da nova população.
'''
populacao_crossover = populacao.drop(indice)
populacao_crossover = populacao_crossover.reset_index(drop=True)


gene_series_1 = populacao_crossover.iloc[0]
gene_series_2 = populacao_crossover.iloc[1]
gene_series_1_concat = pd.concat([gene_series_1[0:4],gene_series_2[4:8]], ignore_index=True)
gene_series_2_concat = pd.concat([gene_series_2[0:4],gene_series_1[4:8]], ignore_index=True)
print(gene_series_1_concat)
print(gene_series_2_concat)
#for x in range(6):
#    gene_series_1 = populacao_crossover.iloc[x]
#    gene_series_2 = populacao_crossover.iloc[x+1]


#for x in range(6):
#    for y in range(8):
#        pass
#Etapa 4.1: Seleção por roleta (Os genes serão selecionados aleatoriamente de forma ponderada, tendo o mais adaptado com
#maiores chances de transmitir seu gene e o menos adaptado com menores chances.)
#nova_geracao = cruzamento(adaptacao.iloc[[1, 2, 3, 4, 5, 6]])
