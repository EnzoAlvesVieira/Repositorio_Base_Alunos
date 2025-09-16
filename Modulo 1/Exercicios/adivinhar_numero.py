from random import randint

numero = randint(1,10)

print('| --------------------MEGASENA-------------------- |')

print('Vou pensar em um número de 1 a 10, tente adivinhar!')
numero1 = int(input('Digite um número: '))

while numero1 != numero:
    print('Você errou! ')
    if numero1 < numero:
        print('⬆️. ')
    else:
        print('Número menor.⬇️ ')
    numero1 = int(input('Digite outro numéro: '))

print('Você acertou! ')
