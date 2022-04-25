# ts = float(input(''))

ts = int(input(''))
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
elif minuto < 60:
   m = minuto
elif hora < 24:
    h = hora
elif dia > 0:
    d = dia

print (f"{d}\n{h}\n{m}\n{s}")