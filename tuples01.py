nums = ("zero", "um", "dois", "três", "quatro", "cinco",
           "seis", "sete", "oito", "nove", "dez", "onze",
           "doze", "treze", "quatorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")

while True:
    userNum = int(input("Digite um número entre 0 e 20: "))
    if 0 <= userNum <= 20:
        break
    print("Número inválido, tente novamente.", end=' ')
print('Você digitou o número {}'.format(nums[userNum]))


