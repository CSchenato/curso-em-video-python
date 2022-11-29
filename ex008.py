# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite a quantidade em metros: '))
#print(f'{n} metro(s) equivale a {n*100} centímetro(s) e {n*1000} milímetro(s)')

# O professor quis acrescessentar mais medidas, vou fazer usando variáveis agora

km = n / 1000   # quilômetro
hm = n / 100    # hectômetro
dam = n / 10    # decâmetro
dm = n * 10     # decímetro
cm = n * 100    # centímetro
mm = n * 1000   # milímetro
print(f'{n} metro(s) equivale a:\n {cm} centímetro(s),\n {mm} milímetro(s)\n', end=' ')
print(f'{dm} decímetro(s)\n {dam} decâmetro(s)\n {hm} hectômetro(s)\n {km} quilômetro(s)')
