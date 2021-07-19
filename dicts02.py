from random import randint
jogadas_dado = {}
for c in range(0, 1):
    jogadas_dado["jogador1"] = randint(1, 6)
    jogadas_dado["jogador2"] = randint(1, 6)
    jogadas_dado["jogador3"] = randint(1, 6)
    jogadas_dado["jogador4"] = randint(1, 6)
print('Valores sorteados:')
for c, v in jogadas_dado.items():
    print(f'  O {c} tirou {v}')
print('Ranking dos jogadores:')
cont = 1
for i in sorted(jogadas_dado, key = jogadas_dado.get):
    print(f'  {cont}º lugar: {i} com {jogadas_dado[i]}')
    cont += 1


