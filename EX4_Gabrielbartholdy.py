#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".   

co = input("Qual sua cor preferida: ")

if co == "vermelho" or co == "VERMELHO" or co == "Vermelho" :
    print("Eu também gosto de vermelho")

else:
   print("Eu não gosto de {}, eu prefiro vermelho".format(co)) 
