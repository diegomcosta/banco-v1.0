print("=" * 40)
menu = """

>>>>> APP DO BANCO <<<<<

MENU PRINCIPAL:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=> """ 

print("=" * 40)

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
lim_saques = 3
depositos = []
saques = []

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")
        deposito = int(input("Entre com a quantidade a depositar em R$"))
        saldo += deposito
        print("Depósito realizado com sucesso!")
        depositos.append(deposito)


    elif opcao == "s":
        print("Saque")
        if qtd_saques > lim_saques:
            print("Você já realizou todos os saques disponíveis para hoje.")
        else:
            saque = (int(input("Entre com a quantidade em R$ que deseja sacar: ")))
            if (saque > 500):
                print("O saque deve ser de no máximo R$500,00\nRetornando ao menu principal...")
            else:
                if (saque <= saldo):
                    print(f"Saque de R${saque} realizado com sucesso.")
                    saques.append(saque)
                    qtd_saques += 1
                    saldo -= saque

                else:
                    print("Você não possui saldo suficiente para realizar este saque.\nRetornando ao menu principal")

    elif opcao == "e":
        print("Extrato")
        if depositos == [] and saques == []:
            print("=" * 20)
            print("Não foram realizadas movimentações")
        else:
            print("=" * 20)
            print("Depósitos realizados: ")
            print()
            for d in depositos:
                print(f"R$ {d}.00")
            print()
            print("=" * 20)
            print("Saques realizados: ")
            print()
            for s in saques:
                print(f"R$ {s}.00")
            print("=" * 20)
            print(f"SALDO EM CONTA: \n\nR${saldo}")
    
    elif opcao == "q":
        print("Obrigado por utilizar o app bancário.")
        print("Saindo...")
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")


