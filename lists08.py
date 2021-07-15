lista7 = [[], []]
valor = 0
for el in range(1, 8):
    valor = int(input(f'Digite o {el}o. valor: '))
    if valor % 2 == 0:
        lista7[0].append(el)
    else:
        lista7[1].append(el)

print(f'Os valores pares digitados foram: {lista7[0]}')
print(f'Os valores ímpares digitados foram: {lista7[1]}')


