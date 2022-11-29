# Desafio 006 - Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Como eu fiz:
n = int(input('Digite um núméro: '))
print(f'O dobro de {n} é {n*2}, o triplo é {n*3}, e sua raiz quadrada é {n**(1/2):.2f}')
# Na raiz quadrada também podemos colocar {n**0.5}. Outra forme é {pow(n,1/2)}, mas dessa forma perde a precedência.
