tempo = int(input('Digite o tempo de uso do seu carro ? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

    #Outra Opção de Resolver#

tempo01 = int(input('Digite quantos nos de uso tem seu carro '))

print('Carro novo' if tempo01 <= 3 else 'carro velho\n')

print('Fim')

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Excelente nota {}, você passou de ano '.format(media))

if media < 7 and media > 5:
    print('Você passou por pouco, sua nota foi {} precisa estudar um pouco mais '.format(media))

else:
    print('{} e uma nota ruim, precisa estudar mais, você não passou de ano '.format(media))


