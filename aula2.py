a = int(input('Entre com o valor de a: '))
b = int(input('Entre com o valor de b: '))
soma = a + b

print(type(soma))

print('resultado : ' + str(soma))
print('resultado : {soma}. \n'
      'subtracao: {subtracao}.'.format(soma=soma, subtracao=(a-b)))