lista = []
numero = input('digite o primeiro numero :').split() #dividir string
for elemento in numero:  
    lista.append(int(elemento))
if lista[0] < lista[1]:
    print(f'{lista[0]} {lista[1]}')
else:
    print(f'{lista[1]} {lista[0]}')