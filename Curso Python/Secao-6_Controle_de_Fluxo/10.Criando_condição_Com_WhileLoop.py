#Publicar um produto com comissão se for 10% se for acima de $20

valor = int(input('Digite o valor do produto? '))

while valor >= 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break