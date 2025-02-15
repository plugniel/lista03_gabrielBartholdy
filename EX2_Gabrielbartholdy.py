#Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais, exiba a mensagem "Muito alto", caso contrário, exiba "Obrigado".

num1 = int(input("Fale um valor inferior a 20: "))

if num1 > 20:
    print("muito alto")
else:
    print("Obrigado")    