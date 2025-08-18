##Elaborar um programa Python para somar os digitos de um número menor que 100
numero = round(float(input('Digite um número menor que 100: ')), 3)

if numero >= 100:
 print('O número deve ser menor que 100.')
else:
    numeroStr = str(numero).split('.')
    inteira, decimal = numeroStr
    inteira = int(inteira)
    decimal = int(decimal)
    
    inteira_dezena = inteira // 10
    inteira_unidade = inteira % 10

    decimal_centena = decimal // 100
    decimal_dezena = (decimal % 100)//10
    decimal_unidade = (decimal % 100) % 10
    
    soma = inteira_dezena+inteira_unidade+decimal_centena+decimal_dezena+decimal_unidade

    print(f"A soma dos algarismos é: {soma}")

##Crux Sacra Sit Mihi Lux