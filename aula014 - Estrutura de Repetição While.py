# Exemplos do uso do While

#Exemplo 01

print('!!!!!Inicio!!!!!')

for contador in range(1, 10):
    print(contador, end=' - ')

#Para representar a mesma estrutura acima, feita com for, no hhile fica assim;

#Exemplo 02

contador01 = 1
while contador01 <= 10:
    print(contador01, end=' - ')
    contador01 = contador01 + 1
print('!!!!Fim!!!!')

#Exemplo 03

numero = int
while numero != 0:
    numero = int(input('Digite um valor: '))
print('!!!!!!Fim!!!!!!!')

#Exemplo 04

resposta = 'S'
numero01 = 0
while resposta == 'S':
    numero01 = int(input('Digite um valor aqui: '))
    resposta = str(input('Deseja continuar? S/N: ')).upper()
print('!!!!Fim!!!!')

#Exemplo 05

numero02 = int
par = 0
impar = 0
while numero02 != 0:
    numero02 = int(input('Digite um valor: '))

    if numero02 != 0:
        if numero02 % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

print('Voce digitou {} numeros par(es) e {} numeros impar(es)'.format(par, impar))

