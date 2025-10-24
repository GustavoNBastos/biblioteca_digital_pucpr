# 🧪 Relatório de Teste — Função listar_documentos()

## 📅 Data do teste
24/10/2025

## 👨‍💻 Responsável
Gustavo Bastos

---

## 🎯 Objetivo do teste
Verificar o funcionamento da função `listar_documentos()` no sistema CLI da Biblioteca Digital, garantindo que os arquivos da pasta `docs/` sejam listados corretamente por tipo de arquivo.

---

## ⚙️ Arquivos testados
- `biblioteca.py` — função `listar_documentos()`
- `main.py` — menu CLI que chama a função
- Pasta `docs/` com arquivos de teste

---

## 🧩 Cenário de teste
1. Estrutura de diretórios:

biblioteca_digital_pucpr/
├── main.py
├── biblioteca.py
├── docs/
│ ├── artigo_2023.pdf
│ ├── tese_2022.pdf
│ └── livro_2021.epub
├── README.md
└── iniciar.bat

yaml
Copiar código

2. Execução do menu CLI via `iniciar.bat`.  
3. Seleção da opção **1 — Listar documentos**.

---

## 🔍 Observações do teste
- A função verifica se a pasta `docs/` existe.  
- Caso a pasta esteja vazia, exibe mensagem apropriada: `Não há documentos na pasta.`  
- Os arquivos foram corretamente agrupados por tipo (`.pdf`, `.epub`).  
- A saída no terminal foi clara e organizada.

---

## ✅ Resultado obtido

Saída esperada / observada:

=== Documentos na Biblioteca ===

Tipo .pdf:

artigo_2023.pdf

tese_2022.pdf

Tipo .epub:

livro_2021.epub

kotlin
Copiar código

- A função funcionou corretamente, exibindo todos os arquivos da pasta `docs/`.  
- Não houve erros nem travamentos no CLI.  

---

## 🧾 Conclusão
- A função `listar_documentos()` está **implementada corretamente e funcional**.  
- Menu CLI agora é capaz de mostrar arquivos reais da pasta `docs/`.  
- Próximo passo: implementar as funções **adicionar**, **renomear** e **remover** documentos.