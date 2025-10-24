# 🧪 Relatório de Testes — Sistema de Biblioteca Digital

## 📅 Data do teste
18/10/2025

## 👨‍💻 Responsável
Gustavo Bastos

---

## 🎯 Objetivo do teste
Verificar o funcionamento da estrutura inicial do sistema de gerenciamento da biblioteca digital, garantindo a comunicação entre os módulos `main.py` e `biblioteca.py`, e o correto funcionamento da interface de linha de comando (CLI).  

---

## ⚙️ Arquivos testados
- `main.py` — menu interativo e lógica principal.  
- `biblioteca.py` — funções de manipulação de documentos (placeholder).  
- `README.md` — instruções de execução.  
- `iniciar.bat` — arquivo de inicialização para usuários finais.  
- `.gitignore` — ignora arquivos temporários e pastas desnecessárias.

---

## 🧩 Cenário de teste
1. Estrutura de diretórios:
biblioteca_digital_pucpr/
├── main.py
├── biblioteca.py
├── docs/
├── README.md
├── iniciar.bat
└── .gitignore

yaml
Copiar código

2. Execução inicial no **PowerShell** (VS Code).  
- Menu era exibido, mas **não reagia após digitar opções** devido ao comportamento do PowerShell com `input()`.  

---

## 🔍 Análise do problema
- Limitação do PowerShell: entrada via `input()` pode travar ou não registrar a digitação.  

---

## 🧭 Ações corretivas
1. Criado **iniciar.bat** para executar o programa no Prompt de Comando (cmd).  
2. Atualizado **README.md** com instruções detalhadas de execução.  
3. Adicionado **.gitignore** para ignorar arquivos temporários (`__pycache__/`, `*.pyc`, `venv/`, etc.).

---

## ✅ Resultado obtido
- Menu CLI funciona normalmente via `iniciar.bat` ou cmd.  
- Funções placeholder chamam mensagens corretas:

=== Sistema de Gerenciamento de Biblioteca Digital ===

Listar documentos

Adicionar documento

Renomear documento

Remover documento

Sair
Escolha uma opção: 1

[Em desenvolvimento] - Função para listar documentos.

yaml
Copiar código

- Arquivos temporários do Python não aparecem mais no Git.  

---

## 🧾 Conclusão
- Estrutura do sistema funcional.  
- Menu CLI confiável para usuários finais.  
- `iniciar.bat` simplifica execução e elimina problemas do PowerShell.  
- Documentação atualizada e repositório limpo.  
- Próximo passo: implementar `listar_documentos()` para mostrar arquivos reais na pasta `docs`.