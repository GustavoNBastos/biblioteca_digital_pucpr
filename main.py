from biblioteca import (
    listar_documentos,
    adicionar_documento,
    renomear_documento,
    remover_documento
)

def exibir_menu():
    print("\n=== Biblioteca Digital PUCPR ===")
    print("1. Listar documentos")
    print("2. Adicionar documento")
    print("3. Renomear documento")
    print("4. Remover documento")
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
        elif opcao == "0":
            print("👋 Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
