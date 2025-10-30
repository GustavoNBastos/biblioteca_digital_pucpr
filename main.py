from biblioteca import (
    listar_documentos,
    adicionar_documento,
    renomear_documento,
    remover_documento,
    restaurar_documento,
    Cores
)

def exibir_menu():
    print(f"\n{Cores.INFO}=== Biblioteca Digital PUCPR ==={Cores.RESET}")
    print("1. Listar documentos")
    print("2. Adicionar documento")
    print("3. Renomear documento")
    print("4. Remover documento")
    print("5. Restaurar documento da lixeira")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_documentos()
        elif opcao == "2":
            adicionar_documento()
        elif opcao == "3":
            renomear_documento()
        elif opcao == "4":
            remover_documento()
        elif opcao == "5":
            restaurar_documento()
        elif opcao == "0":
            print(f"{Cores.INFO}👋 Encerrando o sistema. Até logo!{Cores.RESET}")
            break
        else:
            print(f"{Cores.ERRO}❌ Opção inválida. Tente novamente.{Cores.RESET}")

if __name__ == "__main__":
    main()
