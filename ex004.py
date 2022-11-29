# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

n = input('Digite qualquer coisa: ')
print(type(n))
print('É um número?', n.isnumeric())             # verifica se é um número (apenas números)
print('Tem letras ou números?', n.isalnum())     # verifica se é alfanumérico (pode conter tanto letras como números)
print('Tem letra?', n.isalpha())                 # verifica se é alfabético (apenas letras)
print('Tem espaços?', n.isspace())               # verifica se tem espaços
print('Tem letra maiúscula?', n.islower())       # verifica se só tem letras minúsculas
print('Tem letra minúscula?', n.isupper())       # verifica se só tem letras maiúsculas
print('Está caitalizada?', n.istitle())          # verifica se está capitalizada, ou seja, se tem letras maiúsculas ou minúsculas
