lista_num = []
for el in range(0, 5):
    n = int(input('Digite um valor: '))
    if el == 0 or n > lista_num[-1]:
        lista_num.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista_num):
            if n <= lista_num[pos]:
                lista_num.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados foram {lista_num} (de forma ordenada).')        
        
        
      
    