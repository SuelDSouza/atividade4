opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    item = input("Digite o nome do item a ser adicionado: ")
    lista_compras.append(item)
    print("Item adicionado à lista de compras.")

elif opcao == "2":
    if len(lista_compras) == 0:
        print("A lista está vazia.")
    else:
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido da lista de compras.")
        else:
            print("O item não está na lista de compras.")

elif opcao == "3":
    if len(lista_compras) == 0:
        print("A lista está vazia.")
    else:
        print("Itens da lista de compras:")
        for item in lista_compras:
            print("- " + item)

elif opcao == "4":
    lista_compras.clear()
    print("Lista de compras limpa.")

elif opcao == "5":
    break

else:
    print("Opção inválida. Por favor, digite um número de 1 a 5.")