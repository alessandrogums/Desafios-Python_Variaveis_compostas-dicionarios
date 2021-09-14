#  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#   Depois vai ler a quantidade de gols feitos em cada partida. 
#   No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogo={}
gols=[]
jogo['jogador']=str(input('digite o nome do jogador:'))
partidas=int(input(f'quantas partidas o {jogo["jogador"]} jogou:'))
for c in range(1,partidas+1):
    gol=int(input(f'quantos gols foram feitos na partida nº{c}:'))
    gols.append(gol)
jogo['gols']=gols
jogo['total']=sum(gols)
print('='*30)
print(jogo)
print('='*30)
for k,v in jogo.items():
    print(f'{k} é igual a {v}')
print('='*30)
print(f'o jogador {jogo["jogador"]} jogou {partidas} partidas')
cont=0
for v in jogo['gols']:
    print(f'no jogo nº{cont+1} ele fez {v} gols')
    cont+=1
print('='*30)
