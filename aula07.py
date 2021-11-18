nome = input('Qual seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome), end=' ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2
mult = num1 * num2
Div = num1 / num2
DivInt = num1 // num2
RestDiv = num1 % num2
Expo = num1 ** num2

print('Soma vale {},A multiplicação {},A divisão vale {},A divisão Inteira vale {},O resto da divisão vale {},A exponeciação vale {}'.format(soma, mult, Div, DivInt, RestDiv, Expo))
print('Soma vale {}, \n A multiplicação {} ,\n A divisão vale {:.3f},\n A divisão Inteira vale {},\n O resto da divisão vale {},\n A exponeciação vale {}'.format(soma, mult, Div, DivInt, RestDiv, Expo))

print('Soma vale {}'.format(soma))
print('A multiplicação {}'.format(mult))
print('A divisão vale {:.3f}'.format(Div))
print('A divisão Inteira vale {}'.format(DivInt))
print('O resto da divisão vale {}'.format(RestDiv))
print('A exponeciação vale {}'.format(Expo))
