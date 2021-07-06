nums = ("zero", "um", "dois", "três", "quatro", "cinco",
           "seis", "sete", "oito", "nove", "dez", "onze",
           "doze", "treze", "quatorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")

userNum = int(input("Digite um número entre 0 e 20: "))
if userNum < 0 or userNum > 20:
    userNum = int(input("Número inválido, tente novamente. Digite um número: ")) 
print('Você digitou o número {}'.format(nums[userNum]))
