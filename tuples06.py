t = ('violao', 'guitarra', 'bateria', 'baixo', 'teclado')
cont = 0
for elements in t:
    print(f'Na palavra {t[cont]} temos as vogais:', end=' ')
    if 'a' in t[cont]:
        print('a', end=' ')
    if 'e' in t[cont]:
        print('e', end=' ')
    if 'i' in t[cont]:
        print('i', end=' ')
    if 'o' in t[cont]:
        print('o', end=' ')
    if 'u' in t[cont]:
        print('u', end=' ')
    cont += 1
    print('\n')
 