#Encontrar raízes reais para equações do segundo grau
import math as m

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
delta = (b**2) - 4*a*c

if delta < 0:
    print('Não há raízes reais.')

x1 = round((-b + m.sqrt(delta))/2*a, 2)
x2 = round((-b - m.sqrt(delta))/2*a, 2)

if b >= 0 and c >= 0:
    print(f'{x1} e {x2} são as raízes para {a}x²+{b}x+{c}')
elif b >= 0 and c < 0:
    print(f'{x1} e {x2} são as raízes para {a}x²+{b}x{c}')
elif b < 0 and c >= 0:
    print(f'{x1} e {x2} são as raízes para {a}x²{b}x+{c}')