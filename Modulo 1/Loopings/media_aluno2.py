print('SISTEMA DE PROVAS')
nome = input('Digite o Nome do Aluno: ')
numero_de_provas = int(input('Quantas Provas o Aluno Realizou: '))
contador = 1
soma = 0

while contador <= numero_de_provas:
    nota = float(input(f'Digite a Nota da Primeira Prova {contador}:  '))
    contador = contador + 1
    soma = soma + nota
media = soma / numero_de_provas    
print(f'A Média do Aluno {nome} é {media:.2f} ')