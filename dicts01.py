aluno = dict()
for c in range(0, 1):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
if aluno["media"] >= 7:
    print('A situação é APROVADO')
else:
    print('A situação é REPROVADO')


