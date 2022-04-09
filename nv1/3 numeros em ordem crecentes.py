numero1 = 3
numero2 = 2
numero3 = 1

maiorNumero = 0
meioNumero = 0
menorNumero = 0

for numero in numero1, numero2, numero3:
    if numero > maiorNumero:
        menorNumero = maiorNumero
        print(menorNumero,'menor numero')
        maiorNumero = numero
        print(maiorNumero,'maior numero')
    elif numero < maiorNumero:
        if numero > menorNumero:
            meioNumero = numero
            print(meioNumero, 'medio numero')
        else:
            meioNumero = menorNumero
            print(meioNumero, 'medio numero')
            menorNumero = numero
            print(menorNumero,'menor numero')

print(f'{menorNumero}\n{meioNumero}\n{maiorNumero}')