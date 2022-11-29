# Desafio 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

# Como eu fiz:

print('Digite seu nome: ')

nome = input()

print('É um prazer te conhecer,', nome, '!')

# Maneira mais elaborada de fazer:

nome = input('Digite seu nome: ')

print('É uma prazer te conhecer, {}!'.format(nome))
