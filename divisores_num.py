entrada = int(input('Digite um número: '))

candidatos = range(1,entrada+1)

for numero in candidatos:
    if entrada % numero == 0:
        print(f'{numero} é um divisor de {entrada}')