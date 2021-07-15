matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''matriz = [[], [], []]

c0 = c1 = c2 = 0
while True:
    for el in range(0, 3):
        matriz[0].append(int(input(f'Digite um valor para [0, {c0}]: ')))
        c0 += 1
    for el in range(0, 3):
        matriz[1].append(int(input(f'Digite um valor para [1, {c1}]: ')))
        c1 += 1
    for el in range(0, 3):
        matriz[2].append(int(input(f'Digite um valor para [2, {c2}]: ')))
        c2 += 1        
    break

print('-'*30)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')'''


