#Essa e a estrutura que estudamos, e agora vamos ver como fazer ela usando o break
contador = 1
while contador <= 10:
    print(contador, ' - ', end='')
    contador = contador + 1
    #contador += 1
print('Acabou')

numero = soma = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        break
    soma = soma + numero
    #soma += numero
print('a soma dos valores e de {}'.format(soma))

# Uso das F-strings #

print(f'\na soma dos valores e de {soma}')

nome = 'Jose'
idade = 33
salario = 987.35
print(f'\nO {nome:-^10} tem {idade} anos e ganha R${salario:.2f}')

#todas as formatações funcionan dentro das f-strings

