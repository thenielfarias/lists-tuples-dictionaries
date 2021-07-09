instruments = ('violao', 'guitarra', 'bateria', 'baixo', 'teclado')
for words in instruments:
    print(f'\nNa palavra {words.upper()} temos as vogais:', end=' ')
    for letters in words:
        if letters.lower() in 'aeiou':
            print(letters, end=' ')

