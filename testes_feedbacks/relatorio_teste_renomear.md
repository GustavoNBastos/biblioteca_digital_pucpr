# Relatório de Teste: Função renomear_documento()

**Data:** 30/10/2025  
**Responsável pelo Teste:** Gustavo  
**Arquivo Testado:** `biblioteca.py`  
**Função:** `renomear_documento()`

---

## Objetivo
Testar a funcionalidade de renomear documentos, garantindo que:
- O documento seja renomeado de acordo com o novo título e ano fornecidos.
- O tipo seja detectado automaticamente pela extensão.
- Não ocorra sobrescrita de arquivos existentes.

---

## Ambiente de Teste
- Sistema Operacional: Windows 10  
- Python: 3.13  
- Pasta de documentos: `docs/`

---

## Etapas de Teste

| Etapa | Ação | Resultado Esperado | Resultado Obtido |
|-------|------|------------------|-----------------|
| 1 | Executar o sistema (`iniciar.bat`) e escolher a opção 3 - Renomear documento | Lista todos os documentos disponíveis | ✅ Conforme esperado |
| 2 | Selecionar arquivo: `Inteligência_Artificial_artigo_2025.pdf` | Solicita novo título e ano | ✅ Conforme esperado |
| 3 | Informar novo título: `Machine Learning` e novo ano: `2026` | Detecta extensão `.pdf`, tipo `artigo` e gera novo nome padronizado | ✅ Conforme esperado |
| 4 | Verificar a pasta `docs/` | Arquivo renomeado para `Machine_Learning_artigo_2026.pdf` | ✅ Conforme esperado |

---

## Observações
- A função detecta automaticamente o tipo do documento com base na extensão.
- Caso o arquivo já exista com o novo nome, a operação é cancelada para evitar sobrescrita.
- Teste realizado com sucesso, renomeação concluída sem erros.

---

## Conclusão
A função `renomear_documento()` está funcionando corretamente e atende aos requisitos de padronização e segurança.

