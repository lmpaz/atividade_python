# ts = float(input(''))

ts = 140
segundo = ts
minuto = int(ts /60)
hora = int(minuto /60)
dia = int(hora /24)

d = 0
h = 0
m = 0
s = 0 


if segundo < 60:
    s = ts
elif minuto <= 59:
   m = minuto
   s = (minuto*10)
   

print (f"{d}\n{h}\n{m}\n{s}")