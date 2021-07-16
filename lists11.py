ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-'*25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*25)
    notas_aluno = int(input('Digite o No. do aluno para ver suas notas ou 999 para sair '))
    if notas_aluno == 999:
        print('FINALIZANDO...')
        break
    if notas_aluno <= len(ficha)-1:
        print(f'Notas de {ficha[notas_aluno][0]} são {ficha[notas_aluno][1]}')


