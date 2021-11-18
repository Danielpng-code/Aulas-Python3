nome = str(input('Qual e seu nome ? ')).upper()

if nome == "DANIEL":
    print('Que belo nome {}, seu nome e mto bonito, bom dia!!!'.format(nome))

elif nome == 'BENJAMIN' or nome == 'AMELIE' or nome == 'CATARINA' or nome == 'CERBERUS' or nome == 'FUMAÇA':
    print('Maravilhoso nome seu dog dog {} tem'.format(nome))

elif nome == 'NEGÃO' or nome == 'RAJADO':
    print('{}, maldição de cachorro que batinham no Cerberus'.format(nome))

elif nome in 'FRED BELINHA PELE':
    print('{} e um nome bonito de catiorros'.format(nome))

else:
    print('Não gostei do seu nome não, {}!!!'.format(nome))

print('\nTenha um bom dia!!!!')


