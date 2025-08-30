menu = """
=================== MENU ===================

Operações disponíveis:
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

============================================

Digite a letra da operação que deseja realizar: 

>>> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print(f"\nOperação realizada com sucesso!\n\nValor depositado foi de: R$ {valor: .2f}.\nSaldo atual é de: {saldo: .2f}.\n")

        else:
            print("\nValor de depósito inválido. O depósito mínimo é de R$ 0,1.\n\n")
       
        
    elif opcao == "S":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor de saque excede o limite máximo de saque que é de R$ 500,00 por saque.")

        elif excedeu_saques:
            print("\nOperação falhou! O limite de saques excedeu o limite máximo de 3 saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1
            print(f"\nOperação realizada com sucesso!\n\nValor sacado foi de: R$ {valor: .2f}.\nSaldo atual é de: {saldo: .2f}.\n")

        else:
            print("\nValor de saque inválido. O saque mínimo é de R$ 1,00.\n\n")         

    elif opcao == "E":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas movimentações financeiras." if not extrato else extrato)
        print(f"\nSaldo atual: {saldo: .2f}\n")
        print("=================================================")   

    elif opcao == "Q":
        break

    else:
        print("\nOpção inválida. Por favor, selecione novamente a operação desejada.")
