# 🧪 Relatório de Teste — Função 

`adicionar_documento()`

## 📘 Identificação
- **Projeto:** Biblioteca Digital PUCPR  
- **Diretório:** `/testes_feedbacks/`  
- **Arquivo:** `biblioteca.py`  
- **Função testada:** `adicionar_documento()`  
- **Data do teste:** 30/10/2025  
- **Responsável:** Gustavo Bastos  

---

## 🎯 Objetivo do teste
Validar o correto funcionamento da função `adicionar_documento()`, assegurando que o sistema:
- Solicite apenas **título** e **ano de publicação**;  
- Permita o **arraste e soltura de arquivos** diretamente no terminal;  
- **Identifique automaticamente o tipo** de documento pela extensão;  
- Gere **nomes padronizados** e **salve corretamente** os arquivos na pasta `docs/`.

---

## ⚙️ Procedimento
1. Execução do sistema via `iniciar.bat`.  
2. Seleção da opção `2 - Adicionar documento`.  
3. Entrada de dados:
   - **Título:** Inteligência Artificial  
   - **Ano:** 2025  
4. Arquivo arrastado para o terminal:  
C:\Users\user\Documents\IA.pdf

yaml
Copiar código
5. Pressionado **Enter** para confirmar o upload.  

---

## 🧩 Resultado esperado
O sistema deve:
- Reconhecer o arquivo `.pdf` como **artigo**;  
- Copiar o arquivo para `docs/`;  
- Gerar o nome padronizado:
Inteligência_Artificial_artigo_2025.pdf

diff
Copiar código
- Exibir mensagem de confirmação:
✅ Documento 'Inteligência_Artificial_artigo_2025.pdf' adicionado com sucesso à biblioteca!

yaml
Copiar código

---

## 📊 Resultado obtido

| Etapa | Descrição | Resultado |
|-------|------------|------------|
| Criação automática da pasta `docs/` | OK | ✅ |
| Entrada de título e ano | OK | ✅ |
| Detecção automática do tipo (`.pdf → artigo`) | OK | ✅ |
| Geração de nome padronizado | OK | ✅ |
| Cópia do arquivo para pasta | OK | ✅ |
| Mensagem de confirmação exibida | OK | ✅ |

---

## 🧠 Conclusão
✅ **Teste aprovado com sucesso.**  
A função `adicionar_documento()` funciona de forma eficiente e sem erros, automatizando a inserção de novos documentos na biblioteca digital com detecção inteligente de tipo de arquivo.

---

## 📚 Próximos passos
- Implementar e testar a função `renomear_documento()`.  
- Criar relatório de teste correspondente (`relatorio_teste_renomear.md`).  
- Subir as alterações para o repositório GitHub.