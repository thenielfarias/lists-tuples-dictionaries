aproveitamento_jogador = {}
lista_gols = []
total_gols = 0

aproveitamento_jogador["nome"] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento_jogador["nome"]} jogou? '))

for i in range(1, (partidas+1)):
    lista_gols.append(int(input(f'Quantos gols na partida {i}? ')))
aproveitamento_jogador["gols"] = lista_gols

for i in lista_gols:
    total_gols += i
aproveitamento_jogador["total"] = total_gols

print('-'*40)
print(aproveitamento_jogador)
print('-'*40)
for c, v in aproveitamento_jogador.items():
    print(f'O campo {c} tem o valor {v}.')
print('-'*40)
print(f'O jogador {aproveitamento_jogador["nome"]} jogou {partidas} partidas.')

for c, v in enumerate(lista_gols):
    print(f'  -> Na partida {(c+1)}, fez {v} gols.')
print(f'Foi um total de {aproveitamento_jogador["total"]} gols.')
