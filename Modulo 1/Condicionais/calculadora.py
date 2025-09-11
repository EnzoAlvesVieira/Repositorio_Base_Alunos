print('|------------------------------')
print('CALCULADORA')
print('|------------------------------')
print('Soma')
print('Subtração')
print('Multiplicação')
print('Divisão')
print('|------------------------------')
opcoes = int(input(f'Digite uma das Opções: '))
numero1 = float(input(f'Digite o Primeiro Número'))
numero2 = float(input(f'Digite o Segundo Número: '))
if opcoes == 1:
    print(f'O Resultado de {numero1} + {numero2} é {numero1 + numero2}')
elif opcoes ==2:
    print(f'O Resultado de {numero1} - {numero2} é {numero1 - numero2}')
elif opcoes ==3:
    print(f'O Resultado de {numero1} X {numero2} é {numero1 * numero2}')
elif opcoes ==4:
    print(f'O Resultado de {numero1} / {numero2} é {numero1 / numero2}')
else:
    print('Erro. Digite um Número novamente')
