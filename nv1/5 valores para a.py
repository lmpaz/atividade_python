#ler 5 valores para x,
#conta quantos deles são negativos
#printar quantos valores foram negativos

numero_negativo = 0
for read in range(0,4):
    numero = int(input(''))
    if numero < 0:
        numero_negativo += 1
print(numero_negativo)

