saldo = 1200
limite = 500
extratoS = 0
extratoD = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    print("""

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
    """)

    opcao = input('=> ')

    if opcao == "1":
        valor = float(input("Insira um valor para depositar: "))

        if valor > 0:
            saldo += valor
            extratoD = valor
            print(f"Depositado {valor} com sucesso!")

        else:
            print("Insira um numero valido!")

    elif opcao == "2":
        valor = float(input("Insira um valor para sacar!: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("O limite maximo de saque é de R$500!")

        elif excedeu_saques:
            print("Você atingiu o numero maximo de saques diarios!")

        elif valor > 0:
            print(f"Você sacou R${valor} com sucesso!")
            saldo -= valor
            extratoS = valor
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Ultimo Deposito: R${extratoD}")
        print(f"Ultimo Saque: {extratoS}")
        print("==========================================")

    elif opcao == "4":
        print("Obrigado por usar nosso sistema! Boa Tarde.")
        break

    else:
        print("Opcão Invalida!")
