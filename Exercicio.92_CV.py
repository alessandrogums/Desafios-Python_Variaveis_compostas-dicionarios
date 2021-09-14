#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dicionario=dict()
nome=str(input('digite seu nome:'))
dicionario['usuario']=nome
ano_nascimento=int(input('digite seu ano de nascimento:'))

while ano_nascimento<0:
    print('digite seu ano de nascimento corretamente')
    ano_nascimento = int(input('digite seu ano de nascimento:'))
    
idade=datetime.now().year-ano_nascimento
dicionario['idade']=idade
carteira_trabalho=int(input('digite sua carteira de trabalho(0 não tem):'))
if carteira_trabalho!=0 and idade>18:
    ano_contratacao=int(input('digite seu ano de contratação:'))
    while ano_contratacao-ano_nascimento < 18:
        print('você está mentindo!Não pode trabalhar com menos de 18 anos')
        ano_contratacao=int(input('digite seu ano de contratação corretamente:'))
    dicionario['ano_contratação']=ano_contratacao
    salario=float(input('digite seu salário:'))
    dicionario['salário']=salario
    idade_aposentadoria=(ano_contratacao+35+idade)-datetime.now().year
    dicionario['idade_aposentadoria']=idade_aposentadoria
    for k,v in dicionario.items():
        print(f'{k} é igual à {v}')
else:
    for k,v in dicionario.items():
        print(f' {k} é igual à {v}')

