# Desafio 003 - Crie uma programa que leia dois números e mostre a soma entre eles

# Como eu fiz:

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
soma = int(n1) + int(n2)
print('A soma dos números é:', soma)

# Maneira mais elaborada de fazer:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
print('A soma dos números entre {} e {}, é igual a {}!'.format(n1, n2, soma))

