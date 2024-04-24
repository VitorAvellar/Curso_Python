compra_confirmada = False
dados_compra = 'compra no valor de 45.48 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada == True:
        print(dados_compra)
        print('Detalhes enviada para o seu e-mail')
        break
else:
    print('falha na compra')