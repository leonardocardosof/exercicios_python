entrada = int(input('Número: '))

contador = entrada
fatores = []

if entrada == 0:
    print('Fatorial: 1')
elif entrada < 0:
    print('Insira um valor maior ou igual a zero.')
else:
    while contador > 0:
        fatores.append(contador)
        contador -= 1

    produto = 1
    for fator in fatores:
        produto = fator*produto

    print(produto)