def menu():
    while True:
        print("\nMenu:")
        print("1 - Exibir Olá")
        print("2 - Exibir Bem-vindo")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção (0 para sair): ")

        if opcao == '1':
            print("Olá!")
        elif opcao == '2':
            print("Bem-vindo!")
        elif opcao == '0':
            print("Saindo...")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o menu
menu()
