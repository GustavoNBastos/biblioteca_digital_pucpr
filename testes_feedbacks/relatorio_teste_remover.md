# Relatório de Teste: Função remover_documento()

**Data:** 30/10/2025  
**Responsável pelo Teste:** Gustavo  
**Arquivo Testado:** `biblioteca.py`  
**Função:** `remover_documento()`

---

## Objetivo
Testar a funcionalidade de remoção de documentos, garantindo que:
- O documento seja removido corretamente da pasta `docs/`.
- A operação peça confirmação antes de excluir.
- Arquivos inexistentes não causem erro.

---

## Ambiente de Teste
- Sistema Operacional: Windows 10  
- Python: 3.13  
- Pasta de documentos: `docs/`

---

## Etapas de Teste

| Etapa | Ação | Resultado Esperado | Resultado Obtido |
|-------|------|------------------|-----------------|
| 1 | Executar o sistema e listar documentos disponíveis | Lista todos os documentos na pasta `docs/` | ✅ Conforme esperado |
| 2 | Selecionar arquivo `Machine_Learning_artigo_2026.pdf` para remoção | Solicita confirmação do usuário | ✅ Conforme esperado |
| 3 | Confirmar remoção digitando `s` | Arquivo removido da pasta `docs/` | ✅ Conforme esperado |
| 4 | Tentar remover um arquivo inexistente `arquivo_inexistente.pdf` | Exibe mensagem de erro sem quebrar o programa | ✅ Conforme esperado |
| 5 | Cancelar remoção digitando `n` | Operação cancelada, arquivo permanece na pasta | ✅ Conforme esperado |

---

## Observações
- A função verifica se o arquivo existe antes de tentar removê-lo.  
- Solicita confirmação explícita para evitar exclusão acidental.  
- Teste realizado com sucesso, todos os comportamentos esperados foram atendidos.

---

## Conclusão
A função `remover_documento()` está funcionando corretamente, garantindo segurança e praticidade na exclusão de arquivos da biblioteca.
