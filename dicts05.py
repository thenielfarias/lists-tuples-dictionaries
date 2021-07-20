pessoa = {}
lista_pessoas = []

while True:
    pessoa["nome"] = str(input('Nome: '))
    pessoa["idade"] = int(input('Idade: '))
    pessoa["sexo"] = str(input('Sexo: [M/F] '))
    lista_pessoas.append(pessoa.copy())
    resp = str(input('Quer continunar? [S/N] '))
    if resp in 'Nn':
        break

soma_idade=0
for el in range(0, len(lista_pessoas)):
    soma_idade += lista_pessoas[el]["idade"] 
media_idade = soma_idade / len(lista_pessoas)

print('-'*30)
print(f'- O grupo tem {len(lista_pessoas)} pessoas.')
print(f'- A média de idade é de {media_idade:.2f} anos.')
print('- Mulheres cadastradas: ', end='')
c2=0
for el in lista_pessoas:
    if lista_pessoas[c2]["sexo"] in 'Ff':
        print(lista_pessoas[c2]["nome"], end=' ')
    c2+=1
print('\n- Lista das pessoas com idade acima da média: ')
c3=0
for el in lista_pessoas:
    if lista_pessoas[c3]["idade"] > media_idade:
        print(f'Nome = {lista_pessoas[c3]["nome"]};',
              f'Idade = {lista_pessoas[c3]["idade"]};',
              f'Sexo = {lista_pessoas[c3]["sexo"]};')
    c3+=1    
print()
