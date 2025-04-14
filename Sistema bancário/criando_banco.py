menu = """

[d] Depositar
[s] Sacar
[e] extrato
[q] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f} \n"
            print(f"\n Você depositou R${valor} com sucesso!\n")
            
        

        else: print("\nOperação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Opss... Você não possui saldo suficiente para realizar essa operação!")

        elif excedeu_limite:
            print("Eita! Parece que você já excedeu seu limite de saque diário. Tente novamente amanhã!")
        
        elif excedeu_saque:
            print("Número máximo de saques atingidos. Tente novamente amanhã!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f} \n"
            numero_saques +=1
            print(f"\n Saque de R${valor} realizado com sucesso!")
        
        else:
            print("Operação falhou! o valor informado é inválido.")
    
    elif opcao == "e":
        print("\n ------------ EXTRATO ------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------------------")
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    


    



   
