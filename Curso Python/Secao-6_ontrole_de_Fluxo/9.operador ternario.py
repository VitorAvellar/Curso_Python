idade = input('Qual a sua idade? ')

# if idade >= 16:
#    resultado = print('Voto permitido')
# else:
#     resultado = print("Não Pode votar!!")
    
resultado = 'Voto Permitido' if int(idade) >= 16 else 'voto não permitido'
print(resultado)