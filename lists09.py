matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_col3 = maior_lin2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]    
    print()
print('=-'*20)
print(f'A soma dos valores pares é {soma_pares}.')
for l in range(0, 3):
    soma_col3 += matriz[l][2]
print(f'A soma dos valores da 3º coluna é {soma_col3}.')
for c in range(0, 3):
    if matriz[1][c] > maior_lin2:
        maior_lin2 = matriz[1][c]
print(f'O maior valor da 2º linha é {maior_lin2}')


