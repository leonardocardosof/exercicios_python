qtd_notas = int(input())
notas_restantes = qtd_notas

qtd100 = notas_restantes // 100
notas_restantes = notas_restantes % 100

qtd50 = notas_restantes // 50
notas_restantes = notas_restantes % 50

qtd20 = notas_restantes // 20
notas_restantes = notas_restantes % 20

qtd10 = notas_restantes // 10
notas_restantes = notas_restantes % 10

qtd5 = notas_restantes // 5
notas_restantes = notas_restantes % 5

qtd2 = notas_restantes // 2
notas_restantes = notas_restantes % 2

qtd1 = notas_restantes

print(qtd_notas)

print(qtd100, "nota(s) de R$ 100,00")
print(qtd50, "nota(s) de R$ 50,00")
print(qtd20, "nota(s) de R$ 20,00")
print(qtd10, "nota(s) de R$ 10,00")
print(qtd5, "nota(s) de R$ 5,00")
print(qtd2, "nota(s) de R$ 2,00")
print(qtd1, "nota(s) de R$ 1,00")