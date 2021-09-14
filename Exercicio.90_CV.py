
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.


boletim=dict()
nome=str(input('digite seu nome:'))
boletim['aluno']=nome
nota=float(input('digite sua nota:'))
if nota >= 7:
    boletim['situacao']='aprovado'
else:
    boletim['situacao']='reprovado'
print(f'o aluno {boletim["aluno"]} está {boletim["situacao"]} ')
