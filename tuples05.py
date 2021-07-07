p = (['Lápis', '1.75'], ['Borracha', '2.00'], ['Caderno', '15.90'], ['Estojo', '25.00'], ['Transferidor', '4.20'],
     ['Compasso', '9.99'], ['Mochila', '120.99'], ['Canetas', '22.30'], ['Livro', '34.90'])

print('-'*38)
print('{:^38}'.format('LISTAGEM DE PREÇOS'))
print('-'*38)

for el1, el2 in p:
    print('{:.<30}{}{:''>7}'.format(el1, ('R$'), el2))

print('-'*38)



