


## 🧩 **2️⃣ — Esqueleto de código inicial**


### **main.py**

from biblioteca import *

def exibir_menu():
  print("\n=== Sistema de Gerenciamento de Biblioteca Digital ===")
  print("1. Listar documentos")
  print("2. Adicionar documento")
  print("3. Renomear documento")
  print("4. Remover documento")
  print("0. Sair")

def main():
  while True:
      exibir_menu()
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
          listar_documentos()
      elif opcao == "2":
          adicionar_documento()
      elif opcao == "3":
          renomear_documento()
      elif opcao == "4":
          remover_documento()
      elif opcao == "0":
          print("Encerrando o sistema. Até logo!")
          break
      else:
          print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()
