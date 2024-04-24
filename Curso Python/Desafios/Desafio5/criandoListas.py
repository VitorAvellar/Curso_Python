n1 = int (input('Digite o primeiro numero: '))
n2 = int (input('Digite o segundo numero: '))

resultado = 0
tipoCalculo = input('Que tipo de conta vao ser? ')


if tipoCalculo == "soma":
    resultado = n1 + n2
    print(resultado)

if tipoCalculo == "sub":
    resultado = n1 - n2
    print(resultado)

if tipoCalculo == "mult":
    resultado = n1 * n2
    print(resultado)
    
if tipoCalculo == "divisao":
    resultado = n1 / n2
    print(resultado)

# soma = n1 + n2
# subtrair = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2
# exponencial = soma ** 2

# print('A soma é: ', soma) 
# print('A subtraçao é: ', subtrair)
# print('A multiplicao é:' , multiplicacao)
# print('A divisao é: ', divisao)
# print('A exponenciacao é: ', exponencial )    