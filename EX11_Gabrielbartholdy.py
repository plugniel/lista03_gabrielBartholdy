# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

dist = float (input("Qual a distancia percorrida?(EM KM)"))

if dist <= 200:
    preco = dist * 0.50
    print("seu Viagem deu: {}R$".format(preco))
elif dist > 200:
    preco = dist * 0.45
    print("seu Viagem deu: {}R$".format(preco))
else :
    print("INVALIDO!!!!")