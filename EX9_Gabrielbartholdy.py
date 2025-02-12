#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.

salario = int(input("Qual seu salario?"))

if salario <= 2259:
    print("dadasd")

elif salario >= 2259.21 and salario <= 2826.65:
    desconto = salario * 0.075
    print("voce teve um desconto de: {}R$".format(desconto))

elif salario >= 2826.66 and salario <= 3751.05:
    desconto = salario * 0.150
    print("voce teve um desconto de: {}R$".format(desconto))

elif salario >= 3751.06 and salario <= 4664.68:
    desconto = salario * 0.220
    print("voce teve um desconto de: {}R$".format(desconto))

else:
    desconto = salario * 0.275
    print("voce teve um desconto de: {}R$".format(desconto))