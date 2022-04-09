# entrada de carro de uma casa
# if entrada 999 stop.
# conta excedente de carro
# atribuir multa
# exibir valor valor total mensal de multa
# exibir quantidade de casas 
# 3 > 1 > 12,89
# 10 > 8 > 8 x 12,89
# 1 > 0 > 0
# 2
# 12,89+12,89*8 2

multa = 12.89
multa_mensal = 0
casa_multada = 0
while True:
    carro = int(input(''))
    if carro == 999:
        break
    elif carro > 2:
        multa_mensal += ((carro - 2)* multa)
        casa_multada += 1
print(f"{multa_mensal:.2f}\n{casa_multada}")