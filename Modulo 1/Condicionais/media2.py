from colorama import init, Fore
init(autoreset=True)
print('|------------------------------')
print('SISTEMA DE PROVAS')
print('|------------------------------')
nome = input(f'Nome do aluno?')
nota1 = float(input(f'Nota da Primeira Prova?'))
nota2 = float(input(f'Nota da Segunda Prova?'))
nota3 = float(input(f'Nota da terceira Prova?'))
print('|------------------------------')
media = (nota1 + nota2 + nota3)/3
if media >=5:
    print(Fore.GREEN+f'Aluno Foi Aprovado')
else:
    print(Fore.RED+f'Aluno Foi Reprovado')
    