temp = {}
aproveitamento_jogadores = []

while True:
    print('-'*40)
    temp["nome"] = str(input('Nome do jogador: '))
    temp["partidas"] = int(input(f'Quantas partidas {temp["nome"]} jogou? '))
    
    lista_gols = []
    for el in range(0, temp["partidas"]):
        lista_gols.append(int(input(f'Fez quantos gols na partida {el+1}? ')))
    temp["gols"] = lista_gols

    tot_gols = 0    
    for el in lista_gols:
        tot_gols += el
    temp["total"] = tot_gols    
    aproveitamento_jogadores.append(temp.copy())
    temp.clear()
    
    resp = str(input('Quer continuar? [S/N] '))
    if resp not in 'Ss':
        break
print('='*50)
print('{:<6}{:<12}{:<14}{:>10}'.format("Cód.", "Nome", "Gols", "Total"))
print('-'*50)
for c, v in enumerate(aproveitamento_jogadores):
    print('{:<6}{:<12}{:<14}{:>6}'.format(c, v["nome"], str(v["gols"]), v["total"]))

while True:
    print('-'*50)
    dadosJogador = int(input('Digite o código do jogador para ver seus dados [999 para sair] '))
    while dadosJogador > len(aproveitamento_jogadores) and dadosJogador != 999:
        print('ERRO! Cógido não encontrado. Tente novamente.')
        print('-'*50)
        dadosJogador = int(input('Digite o código do jogador para ver seus dados [999 para sair] '))
    if dadosJogador == 999:
        print('<< Encerrando >>')
        break    
    lista_gols = []
    cont = 0
    lista_gols = aproveitamento_jogadores[dadosJogador]["gols"]
    print(f'-- LEVANTAMENTO JOGADOR {aproveitamento_jogadores[dadosJogador]["nome"]} --')
    for el in range(aproveitamento_jogadores[dadosJogador]["partidas"]):
        print(f'No jogo {el+1} fez {lista_gols[cont]} gols.')
        cont += 1


