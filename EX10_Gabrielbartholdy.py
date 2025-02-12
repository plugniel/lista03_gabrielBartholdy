#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario =    int(input("Qual seu salario?"))

if salario > 1250: 
    aume = salario * 0.10
    print("voce teve um Aumento de: {}R$".format(aume))

elif salario <= 1250: 
    aume = salario * 0.15
    print("voce teve um Aumento de: {}R$".format(aume))