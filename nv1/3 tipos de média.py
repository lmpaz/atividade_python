#escrever tres notas
#calcular a media gelral
#calcular media pesos 2,2 e 3
#calcular media pesos 1,2 e 2
#resposta colocar medias com 2 decimais.
#float(input(''))



while True:
    nota1 = float(input(''))
    nota2 = float(input(''))
    nota3 = float(input(''))

    media1 = (nota1+nota2+nota3)/3
    media2 = ((nota1*2)+(nota2*2)+(nota3*3))/7
    media3 = ((nota1*1)+(nota2*2)+(nota3*2))/5

    print(f'{media1:.2f}\n{media2:.2f}\n{media3:.2f}\n')