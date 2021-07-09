lista_numeros = list()
maior = 0
menor = 0
for el in range(0, 5):
    lista_numeros.append(input(f'Digite um valor para a posição {el}: '))
    if el == 0:
        maior = menor = lista_numeros[el]
    else:
        if lista_numeros[el] > maior:
            maior = lista_numeros[el]
        if lista_numeros[el] < menor:
            menor = lista_numeros[el]  
    
print(f'Você digitou os valores {lista_numeros}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_numeros):
    if v == menor:
        print(f'{i}...', end='')
print()        
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_numeros):
    if v == maior:
        print(f'{i}...', end='')
print()


