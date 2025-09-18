import textwrap


def menu():
    menu = """\n
    =================== MENU ===================\n
    Operações disponíveis:\n
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato\n
    [NC]\tNova conta
    [NU]\tNovo usuário
    [LC]\tListar contas\n
    [Q]\tSair\n
    ============================================\n
    Digite a letra da operação que deseja realizar: 
    >>> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print(f"\nDepósito realizado com sucesso!\n\nValor depositado foi de: R$ {valor: .2f}.\nSaldo atual: {valor: .2f}")
    else:
        print("\nValor de depósito inválido. Tente novamente.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"\nSaldo insuficiente.\n\nSaldo disponível: R$ {saldo: .2f}")

    elif excedeu_limite:
        print(f"\nO valor de saque excede o limite máximo permitido. O limite máximo de saque é de R$ {limite: .2f}")
    
    elif excedeu_saques:
        print(f"\nTentativa de saque falhou: Número máximo de saques excedido.\n\nNúmero de saques já realizados: {numero_saques}")
    
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t  R$ {valor: .2f}\n"
        print(f"\nSaque realizado com sucesso!\n\nValor sacado: R$ {valor: .2f}\nSaldo atual: R$ {saldo: .2f}")

    else:
        print("\nValor inválido. Tente novamente.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato, numero_saques):
    print("\n================= EXTRATO ==================")
    print("\nSem movimentações realizadas.\n" if not extrato else extrato)
    print(f"Saldo:\tR$ {saldo: .2f}")
    print(f"Saques realizados: {numero_saques}\n")
    print("============================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Usuário já existe com este CPF! Criação de usuário encerrado. ---\n")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o endereço completo (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Conta criada com sucesso! ---")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n--- Usuário não encontrado! Criação de conta encerrado! ---")

    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu().upper()

        if opcao == "D":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato, numero_saques=numero_saques)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
               contas.append(conta)
        
        elif opcao == "NU":
            criar_usuario(usuarios)
        
        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Opção inválida! Escolha novamente outra opção")
            

main()
