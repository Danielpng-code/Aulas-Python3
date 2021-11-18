### Exemplo 01 ###

print('\033[31m Ola, mundo!!!')

print('\033[30;43m Ola, mundo!!!\033[m')

print('\033[1;30;43m Ola, mundo!!!\033[m')

print('\033[1;30;43m Ola, mundo!!!\033[m')

print('\033[4;30;45m Ola, mundo!!!\033[m')

print('\033[7;30m Ola, mundo!!!\033[m')

print('\033[0;33;44m Ola, mundo!!!\033[m')

print('\033[7;33;44m Ola, mundo!!!\033[m')

### Exemplo 02 ###

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))

print('Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m'.format(a,b))

#### Exemplo 03 ####

nome = 'Daniel'
print('Prazer em te conhecer, {}{}{}!!!!'.format('\033[4;34m', nome, '\033[m'))

print('Prazer em te conhecer, {}{}!!!!'.format('\033[4;34m', nome))

### Exemplo 04 ###

nome = 'Daniel'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}


print('Prazer em te conhecer, {}{}{}!!!!'.format('\033[4;34m', nome, '\033[m'))

print('Prazer em te conhecer, {}{}{}!!!!'.format(cores['amarelo'], nome, cores['limpa']))

print('Prazer em te conhecer, {}{}{}!!!!'.format(cores['pretoebranco'], nome, cores['limpa']))



