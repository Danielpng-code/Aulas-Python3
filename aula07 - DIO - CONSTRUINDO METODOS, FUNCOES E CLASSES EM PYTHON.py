#função e tudo que retorna um valor, e metodo tudo aquilo que não retorna valores.
#no python o metodo se chama definição e para chamar essa definição e usado a tag def

def soma (a, b):
    return a + b

def subtracao (a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    return a / b


print('Soma', soma(3, 4))
print('Soma', soma(7, 10))
print('Subtração', subtracao(10, 3))
print('Subtração', subtracao(10, 20))
print('Multiplicação', multiplicacao(10, 2))
print('Multiplicação', multiplicacao(2, 4))
print('Divisão', divisao(10, 5))
print('Divisão', divisao(30, 10))

#=======================================CLASSES EXEMPLO CALCULADORA=====================================================
print('-='*30)
numero1 = int(input('Digite o valor do primeiro numero: '))
nummero2 = int(input('Digite o valor do segunco numero: '))

class Calculadora:
    def __init__(self, numero1, numero2):
        self.valor_a = numero1
        self.valor_b = numero2
    def soma (self):
        return self.valor_a + self.valor_b

    def subtracao (self):
        return self.valor_a - self.valor_b

    def multiplicacao (self):
        return self.valor_a * self.valor_b

    def divisao (self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(numero1, nummero2)
print('-='*30)
print('Valor de a = ', calculadora.valor_a)
print('Valor de b = ', calculadora.valor_b)
print('Soma entre a + b = ', calculadora.soma())
print('Subtração entre a - b = ', calculadora.subtracao())
print('Divisão entre a / b = ', calculadora.divisao())
print('Multiplicação entre a * b = ', calculadora.multiplicacao())

#============================OUTRO USO DE CLASSSE - EXEMPLO TELEVISÃO LIGADA E DESLIGADA================================
print('-='*30)
class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def dimunui_canal(self):
        if self.ligada:
            self.canal -= 1




televisao = Televisão()
print(f'Televisão esta ligada ? {televisao.ligada}')
print('Televisão esta ligada ?', televisao.ligada)
print('Televisão esta ligada ? {}'.format(televisao.ligada))

televisao.power()

print(f'Televisão esta ligada ? {televisao.ligada}')
print('Televisão esta ligada ?', televisao.ligada)
print('Televisão esta ligada ? {}'.format(televisao.ligada))

televisao.power()

print(f'Televisão esta ligada ? {televisao.ligada}')
print('Televisão esta ligada ?', televisao.ligada)
print('Televisão esta ligada ? {}'.format(televisao.ligada))

print(f'Canal: {televisao.canal}')
televisao.power()
print(f'Televisão esta ligada ? {televisao.ligada}')
televisao.aumenta_canal()
televisao.aumenta_canal()
print(f'Canal: {televisao.canal}')
televisao.dimunui_canal()
print(f'Canal: {televisao.canal}')
