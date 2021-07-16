from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGUE NA MEGA SENA')
print('-'*30)
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('~'*5, f' SORTEANDO {qtd_jogos} JOGO(S) ', '~'*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('*'*5, f' BOA SORTE! ', '*'*5)


