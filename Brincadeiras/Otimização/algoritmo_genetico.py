'''
Autor: Daniel Paiva Salles
Sintese: Utilizar a técnica de algoritmo genético para trabalhar a otimização de uma situação hipotética.
Problema proposto: Uma empresa de emplacamento de veículos esta precisando realizar a compra de porcas, parafusos e 
arruelas para repor o estoque. Todos os itens são vendidos em pacotes fechados e valores distintos, e todos os itens
possuem suas versões finas e grossas. O valor dos itens finos são: Porcas(R$30,52), Parafusos(R$28,75), 
Soberbos(R$29,63), Arruelas(R$26,74).
Os itens grossos são: Porcas(R$36,13), Parafusos(R$34,19), Soberbos(R$35,48), Arruelas(R$31,32).
A empresa disponibiliza de 500 reais para a aquisição destes insumos. Deve ser adiquirido todos os itens na maior
quantidade possível, respeitando o dinheiro disponível e adiquirindo todos os itens. 
A proporção de compra para porcas/arruelas/parafusos se da pela proporção seguinte proporção:
Porca/Parafuso= 1:1
Parafuso/Soberbo= 1:1
Soberbo/Arruela= 1:1
Parafuso/Arruela= 1:2
'''
import random

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

#Etapa 0: Funções a serem utilizadas
def cromos():
    return random.randint(0, 50)

#Etapa 1: Inicialização (Criar gene e setar cromossomos aleatórios)
gene = []
cromossomo = [cromos(), cromos(), cromos(), cromos(), cromos(), cromos(), cromos(), cromos()]
for x in range(7):
    gene.append(cromossomo)
print(gene)

#Etapa 2: Fitness (Medir a adaptação dos cromossomos)

