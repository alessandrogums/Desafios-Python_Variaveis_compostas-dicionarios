# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
dicionario={}
lista_num=[]
for c in range(1,5):
    num=randint(1,6)
    lista_num.append(num)
    dicionario[f'jogador{c}']=num
for k,v in dicionario.items():
    print(f'o {k} tirou {v} no dado')
lista_num.sort(reverse=True)
cont=0
print(lista_num)
while cont<=3:
    for k,v in dicionario.items():
        if lista_num[cont] == v:
            print(f'{cont+1}º lugar foi do {k}, com valor {v}')
            cont+=1
            break
