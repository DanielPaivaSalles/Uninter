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
import itertools
import random
import pandas as pd

#Etapas:
# -Inicialização: Setar cromossomos aleatórios
# -Medir a adaptação
# -Elitismo
# -Crossover
# --Roleta
# --Ponto de corte
# -Mutação
# -Ir pra proxima geração

#Definições
#Cada gene terá 8 cromossomos; Cada cromossomo pertencerá ao conjunto dos numeros NATURAIS; Os genes serão agrupados
#em duas partes, os quatro primeiros cromossomos pertencerão ao conjunto fino e os quatro ultimos ao conjunto grosso;
#A ordem dos cromossomos será, nos dois grupos, Parafuso(Pa), Porca(Po), Soberbo(So), Arruela(Ar); Cada população 
#proposta como solução terá 7 genes; O mais bem adaptado será mantido por elitismo.

#Etapa 0: Predefinições a serem usadas no sistema
#O metodo randomizar irá retornar os cromossomos do meu gene
#O metodo adaptabilidade irá retornar o gene mais bem adaptado de forma ponderada, sendo a escala de adaptabilidade
#a ser utilizada como, aproximadamente: 0.5, 0.25, 0.125, 0.625, 0.03125, 0.015625
def randomizar():
    return random.randint(1, 15)

def adaptabilidade(adaptacao):
    adaptacao = adaptacao**2
    adaptacao = adaptacao.sort_values(by=0, ascending=False)
    return adaptacao.sample(n = 1, weights=[1, 2, 4, 8, 16, 32])

#DataFrame/Series com os valores dos itens
VALORES = pd.Series([15, 14, 15, 14, 18, 17, 16, 16])

#Constantes
LIMITE = 1000

#Variaveis auxiliares na iteração dos laços
adaptacao = []
acumulador = 0
indice = 0
flag = True
elitizado = pd.DataFrame()

#Etapa 1: Inicialização (Criar gene/cromossomos e seta valores aleatórios nestes)
cromossomo = []
for x in range(7):
    cromossomo.append([randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar(), randomizar()])

populacao = pd.DataFrame(cromossomo, columns=['ParFin', 'ParGros', 'SobFin', 'SobGros', 'PorFin', 'PorGros', 'ArrFin', 'ArrGros'])

#Etapa 2: Fitness (Medir a adaptação dos cromossomos)
for x in range(7):
    acumulador = 0
    for y in range(8):
        acumulador += populacao.iloc[x, y] * VALORES.iloc[y]
    acumulador -= LIMITE
    adaptacao.append(acumulador)

adaptacao = pd.DataFrame(adaptacao)

#Etapa 3: Elitismo (Vamos passar para a proxima geração o gene que mais se aproximar do ótimo sem ultrapassar o limite
for x in range(7):
    if flag:
        acumulador = adaptacao.iloc[x, 0]
        indice = x
        flag = False
    elif(acumulador**2 >= adaptacao.iloc[x, 0]**2):
        acumulador = adaptacao.iloc[x, 0]
        indice = x


#Etapa 4: Crossover (O gene mais bem adaptado vai ficar na posição 0 do dataframe. Os demais irão trocar as 
#         caracteristicas entre sí)

#Etapa 4.1: Seleção por roleta (Os genes serão selecionados aleatoriamente de forma ponderada, tendo o mais adaptado com
#maiores chances de transmitir seu gene e o menos adaptado com menores chances.)
print(adaptacao.iloc[[0, 1, 2, 3, 4, 5, 6]])
#nova_geracao = adaptabilidade(adaptacao)
