pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('_'*50)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoa(s)')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()
