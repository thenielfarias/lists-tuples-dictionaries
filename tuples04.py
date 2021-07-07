while True:
    try:
        n1 = int(input('Digite um número: '))
        break
    except ValueError:
        print('Reposta inválida, tente novamente.')

while True:
    try:        
        n2 = int(input('Digite mais um número: '))
        break
    except ValueError:
        print('Reposta inválida, tente novamente.')      

while True:
    try:
        n3 = int(input('Digite outro número: '))
        break
    except ValueError:
        print('Reposta inválida, tente novamente.')      
        
while True:
    try:             
        n4 = int(input('Digite um último número: '))
        break
    except ValueError:
        print('Reposta inválida, tente novamente.')
        
t = (n1, n2, n3, n4)

cont9 = 0
if t[0] == 9:
    cont9 += 1
if t[1] == 9:
    cont9 += 1
if t[2] == 9:
    cont9 += 1
if t[3] == 9:
    cont9 += 1

pares = []
if t[0] % 2 == 0:
    pares.append(t[0])
if t[1] % 2 == 0:
    pares.append(t[1])
if t[2] % 2 == 0:
    pares.append(t[2])
if t[3] % 2 == 0:
    pares.append(t[3])

if pares != []:
    print('Os números pares digitados foram: ')
    for el in pares:
        print(el, end='\n')
else:
    print('Não foram digitados números pares.')
    
try:
    primeira_pos3 = t.index(3)
except:
    print('O número três não foi digitado.')

print(f'O número nove foi digitado {cont9} vez(es)')
print(f'O número três foi digitado primeiramente na posição {primeira_pos3}')
