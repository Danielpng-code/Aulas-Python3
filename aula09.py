#Fatiamento#

frase = 'Curso em Video Python'

#frase = frase.replace('Python', 'Android') - nesse caso, ela esta trocando a palavra Python, por Android, se mandar imprimir isso, vai sair ja trocado, pq eu atribui esse comando antes de impimir #
#print (frase) - Sairia - Curso em Video Andoid#

print(len(frase)) # Conta o tamanho da string, conta os espaços tbm #
print(len(frase.strip())) # Conta o tamanha da string, retirando os espaços do inicio e fim, não os do meio #

print(frase[3]) # Printa a letra da terceira posição #
print(frase[9:21]) # Pega do 9 ao 21, sempre mostra um caracter antes do numero final, ou seja, vai ate o espaço 20 #
print(frase[9:21:2]) # Vai do 9 ao 21 pulando de 2 em 2 #
print(frase[:5]) # começa do caracter 0 inicio ate a 4, no caso do exemplo #
print(frase[15:]) # começa do caracter 15 e vai ate o final #
print(frase[9::3]) # no caso do exemplo, vai começar do 9 pulando de 3 em 3 ate o final #
print(frase[::2]) # Usado quando a gente não sabe o inicio e o final, e no caso vai pulando de 2 em 2 do inicio ao final #

print("""Construa um código em Java que tenha uma classe principal e uma outra classe de nome “Soma”. As classes podem ficar dentro do mesmo pacote. O mecanismo do código será:
Escreva um aplicativo em Java que mostra todos os números pares e ímpares de 0 até 100 separados em duas colunas. Segue o exemplo de como a exibição deve ser apresentada na tela:\n""") # Quando se usa as duplas 3 vezes pra abrir e fechar o print, ele vai pegar em caso de um texto grande, no mesmo string a frase toda em um mesmo print #

# Analise #

print(len(frase)) # mostra o cumprimento da frase #
print(frase.count('o')) # conta quantas vezes aparece a letra "o" em minusculo, se a letra o tivesse em maiusculo iria contar as maiusculas #
print(frase.count('o', 0, 13)) # faz uma contagem ja com fatiamento, considere do 0 ate o 12, no caso do exemplo quantas letras 'o" tem #
print(frase.find('deo')) # conta a casa onde começa a sequência 'deo' aparace na frase #
print(frase.upper().count('O')) # Vai transformar no caso a letra 'o', em maiuscula e depois contar quanto o maiusculos tem #
print(frase.find('Androide')) # Retorna o valor -1, quando ele não encontra o paramentro que tu passastes #
print(frase.find('Curso')) # Retorna o valor 0, porque a palavra 'Curso' começa na posição 0, se colocar tipo 'Video' vai mostrar 9 porque Video comoça na posição 9#
print('Curso'in frase) # mostra se tem no caso do exemplo a palavra 'Curso', na frase, retorna true ou false #
print(frase.lower().find('video')) # Nesse caso esta transformado as letras todas em minusculo e depois procurando 'video' no texto #

# Transformação #

print(frase.replace('Python', 'Android')) # vai identificar onde tem a palavra Python na frase, e substituir por Androide, no caso do exemplo #
print(frase.upper()) # Deixa as letras de toda a frase em maiusculas #
print(frase.lower()) # Deixa as letras de toda a frase em minusculos #
print(frase.capitalize()) # Deixa todos os caracteres em minusculos com excessão da primeira letra #
print(frase.title()) # Deixa a primeira letra de todas as palavras em Maiusculo e o restante em minusculo #
print(frase.strip()) # Remove todos os espaços inuteis de uma string, ou seja, os do inicio e fim da frase, que não tem função alguma dentro da frase, as do meio de separação das palavras continuam #
print(frase.rstrip()) # Quando na funcionalidade tem o "R" na frente, ele começa a tratar a string somente na direita #
print(frase.lstrip()) # Quando na funcionalidade tem o "L" na frente, ele começa a tratar a string somente na esquerda #


# Divisão #

print(frase.split()) # Divide a string, considerando os espaços #
divido = frase.split() # Criou a variavel dividido e transformou ela em split, igual acima, depois imprimiu a frase #
print(divido)
print(divido[0]) # Mostra o item 0 da lista #
print(divido[2][3]) # Mostra o item 2 que e 'Video' da lista, e posteriormente a terceira letra #

# Junção #

print('-'.join(frase)) # Junta as palavras utilizando como separação o traço que foi pre-repaçado #
print('+'.join(frase)) # Junta as palavras utilizando como separação o traço que foi pre-repaçado, coloquei outro simbolo #
