#Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se ele inserir um número dentro desse intervalo, exiba a mensagem "Obrigado", caso contrário, exiba a mensagem "Resposta incorreta".
num1 = int(input("Insira um numero de 10 a 20:"))

if num1 >= 10 :
    print("obrigado")
elif  num1 <= 20:
    print("obrigado")
else:
    print("Resposta incorreta")