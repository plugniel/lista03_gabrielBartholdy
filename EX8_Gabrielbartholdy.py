#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
velo = int (input("Qual a velocidade do carro?"))

if velo > 80:
    ultr = velo - 80
    multa = ultr  * 5
    print("você recebeu uma Multa de : {}R$".format(multa))
else:
    print("Você esta no limite")
