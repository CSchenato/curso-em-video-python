# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# Como eu fiz:

n = int(input('Digite um número: '))
sucessor = n + 1
antecessor = n - 1
# print('O antecessor de {} é {}, e o sucessor é {}'.format(n, antecessor, sucessor))
print(f'O antecessor de {n} é {antecessor}, e o sucessor é {sucessor}')  # Faz a mesma coisa que a de cima, mas essa é mais usual atualemente

# Como nesse curso o professor está usando Python 3, vou deixar comentado para me basear.

# Resoposta do professor:

n = int(input('Digite um número: '))
#print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(n, (n-1), (n+1)))
print(f'Analisando o valor {n}, seu antecessor é {n-1} e seu sucessor é {n+1}.') # deixei de acordo com o Python 3.7

# Aqui o professor ensina a utilizar menos memória, utilizando menos variáveis, pois nesse caso, não precisaremos delas posteriormente.