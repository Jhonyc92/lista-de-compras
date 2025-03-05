# Inicializa a lista de compras vazia
lista = []

add = []

remove = []

# Loop principal para manter o programa em execução
while True:

    print("Menu")

    print("1. Adicionar item à lista")

    print("2. Remover item da lista")

    print("3. Exibir lista de compras")

    print("4. Sair")

    print()

    # Solicita ao usuário que escolha uma opção do menu
    op = input("Escolha a opção desejada: ")

    print()

    # Se a opção escolhida for 1:
    if op == "1":

        # Solicita o item a ser adicionado
        add = input("Insira o item que deseja adicionar à lista: ")

        print()

        # Adiciona o item à lista de compras utilizando o método append()
        lista.append(add)

        print(f"O item {add} foi adicionado à lista com sucesso!")

        print()

        add = []

    # Se a opção escolhida for 2:
    elif op == "2":

        # Verifica se a lista de compras está vazia
        if lista == []:

            print("A lista de compras está vazia no momento!")

            print()

        else:

            # Solicita o item a ser removido
            remove = input("Insira o item que deseja remover da lista: ")

            print()

            # Verifica se o item está presente na lista
            if remove in lista:

                # Remove o item da lista utilizando o método remove()
                lista.remove(remove)

                print(f"O item {remove} foi removida da lista com sucesso!")

                print()

                remove = []

            else:

                print(f"O item {remove} não está na lista!")

                print()

                remove = []

    # Se a opção escolhida for 3:
    elif op == "3":

        print("Lista de Compras:")

        # Verifica se a lista de compras está vazia
        if lista == []:

            print("A lista de compras está vazia no momento!")

            print()

        else:

            # Itera sobre os itens da lista de compras
            for item in lista:

                # Imprime cada item com um hífen no início
                print("-", item)

            print()

    # Se a opção escolhida for 4:
    elif op == "4":

        print("Encerrando o Programa Lista de Compras!")

        print()

        # Encerra o loop e sai do programa
        break

    # Se a opção escolhida não for válida:
    else:

        print("Opção Inválida!")

        # Adiciona uma linha em branco após cada operação
        print()
    

            
