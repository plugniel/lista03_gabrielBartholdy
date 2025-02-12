#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".

tempo = input("Esta chovendo?").lower()

if tempo=="sim".lower():
    vento = input("Esta ventando?").lower()
    if vento=="sim".lower():
        print("Está ventando muito para um guarda-chuva")
    else:
        print("Pegue um guarda-chuvasi")
else:
    print("Aproveite o seu dia")