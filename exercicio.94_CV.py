#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre:
 # A) Quantas pessoas foram cadastradas 
 #B) A média de idade 
 #C) Uma lista com as mulheres 
 #D) Uma lista de pessoas com idade acima da média

cadastro={}
lista=[]
lista_mulheres=[]

while True:
    cadastro['nome']=str(input('Nome:'))
    cadastro['sexo']=str(input('Sexo: [M/F]-')).strip().upper()[0]

    while not 'M' in cadastro['sexo'] and not 'F' in cadastro['sexo']:
        print('você digitou incorretamente seu sexo')
        cadastro['sexo'] = str(input('Sexo: [M/F]-')).strip().upper()[0]

    cadastro['idade']=int(input('idade:'))
    lista.append(cadastro.copy())
    escolha=str(input('quer continuar?: [S/N]-')).strip().upper()[0]

    if escolha == 'N':
        break

if len(lista) == 1:
    print('foi cadastrada somente 1 pessoa')
else:
    print(f'foram cadastradas {len(lista)} pessoas')

idade=0
for individuo in lista:
    idade+=individuo['idade']
    if 'F' in individuo['sexo']:
        lista_mulheres.append(individuo['nome'])
media_idade=(idade/(len(lista)))
print(f'a média das idades foi de:{media_idade:.2f}')
if len(lista_mulheres) == 0:
    print('não foi cadastrada nenhuma mulher')
else:
    print(f'o nome das mulheres que foram cadastradas:',end=' ')
    for mulheres in lista_mulheres:
        print(mulheres,end=' ')
print('\nAs pessoas que tem idade acima da média:',end=' ')
    if individuo['idade'] > media_idade:
        print(individuo['nome'],end=' ')

