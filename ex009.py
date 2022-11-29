# Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# Como eu fiz:
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*13)
print(f' {n} x  1 = {n*1}\n {n} x  2 = {n*2}\n {n} x  3 = {n*3}\n {n} x  4 = {n*4}\n {n} x  5 = {n*5}')
print(f' {n} x  6 = {n*6}\n {n} x  7 = {n*7}\n {n} x  8 = {n*8}\n {n} x  9 = {n*9}\n {n} x 10 = {n*10}')
print('-'*13)

# O professor fez um pouco diferente, lembrando que ele usa Python 3, segue:
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*7))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)

