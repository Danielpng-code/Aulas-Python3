import math
import emoji
import random
from math import sqrt, floor

num = int(input('Digite m número: '))
raiz = math.sqrt(num)
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

num1 = random.random()
num2 = random.randint(1, 10)

print(num1)
print(num2)


print(emoji.emojize('Ola mundo :earth_americas:', use_aliases=True))