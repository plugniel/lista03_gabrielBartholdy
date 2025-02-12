#Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria", se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".

idade = int (input("Quantos anos você tem?"))
if idade >= 18:
    print("Você pode votar")
    print("Você pode aprender a dirigir")
elif idade >= 16:
    print("Você pode votar")
elif idade <= 14 :
    print("Você pode comprar um bilhete de loteria")
else:
    print("Você pode fazer doces ou travessuras")
