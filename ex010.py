# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# A cotação do Dollar hj, 28/11/22 US$ 5.37
din = float(input('Quanto de dinheiro você tem em sua carteira? R$ '))
print(f'Com {din}, você pode comprar US$ {din/5.37:.2f}.')


#Decidi fazer um onde o usuário tem que digitar a cotação do Dolár no dia

din = float(input('Quanto de dinheiro você tem em sua carteira? '))
dol = float(input('Qual a cotação do Dólar hoje? '))
print(f'Com {din}, você pode comprar US$ {din/dol:.2f}.')

