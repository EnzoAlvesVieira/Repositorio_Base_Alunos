modelo = input('Qual Modelo Do Carro? :')
dias =int(input('Por quantos dias o Carro foi alugado: '))
km = float(input('Quantos quilometros foram rodados? :'))
if modelo == 'Bmw':
    diaria = 150
elif modelo == 'Ferrari':
    diaria = 250
elif modelo == 'Uno':
    diaria = 25
else:
    diaria = 60
total_dias = dias * diaria
total_km = km * 0.50
valor_total = total_dias + total_km
print(f'Você percorreu {km} Km por {dias} dias, então o preço a pagar é R$ {valor_total} ! ')
