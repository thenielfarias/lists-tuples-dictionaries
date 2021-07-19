from datetime import date
ano_atual = date.today().year
cadastro_empregado = {}
for el in range(0, 1):
    cadastro_empregado["nome"] = str(input('Nome: '))
    cadastro_empregado["nasc"] = int(input('Ano de Nascimento: '))
    cadastro_empregado["ctps"] = int(input('Nº carteira de trabalho (0 não tem): '))
    if cadastro_empregado["ctps"] == 0:
        print('-'*40)
        print(f'Nome tem o valor {cadastro_empregado["nome"]}')
        print(f'Idade tem o valor {ano_atual - cadastro_empregado["nasc"]}')
        print(f'CTPS tem o valor 0')
    else:
        cadastro_empregado["admi"] = int(input('Ano de Contratação: '))
        cadastro_empregado["sal"] = float(input('Salário: R$ '))    
        print('-'*40)
        print(f'Nome tem o valor {cadastro_empregado["nome"]}')
        print(f'Idade tem o valor {ano_atual - cadastro_empregado["nasc"]}')
        print(f'Nº CTPS tem o valor {cadastro_empregado["ctps"]}')
        print(f'Ano de contratação tem o valor {cadastro_empregado["admi"]}')
        print(f'Salário tem o valor {cadastro_empregado["sal"]}')
        print(f'Idade aposentadoria tem o valor {(ano_atual - cadastro_empregado["nasc"])+35}')


