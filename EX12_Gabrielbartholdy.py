#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. 

opc = input("Qual a operação desejada?(/)(*)(-)(+)")
num1 = int(input("Qual o primeiro numero?"))
num2 = int(input("Qual o primeiro numero?"))

if opc == "/":

    opera = num1 / num2
    print("Seu Resultado deu: {}".format(opera))

elif opc == "*":

    opera = num1 * num2
    print("Seu Resultado deu: {}".format(opera))

elif opc == "-":

    opera = num1 - num2
    print("Seu Resultado deu: {}".format(opera))

elif opc == "+":

    opera = num1 * num2
    print("Seu Resultado deu: {}".format(opera))
else:
    print("OPERAÇÃO INEXISTENTE")