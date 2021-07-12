listAll = list()
listEven = list()
listOdd = list()
while True:
    listAll.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp not in 'Ss':
        break
print(f'A lista completa de números digitados é: {listAll}')
for el in listAll:
    if el % 2 == 0:
        listEven.append(el)
    else:
        listOdd.append(el)
print(f'A lista de números pares digitados é: {listEven}')
print(f'A lista de números ímpares digitados é: {listOdd}')