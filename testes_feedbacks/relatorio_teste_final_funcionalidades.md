# Relatório de Teste – Sistema de Biblioteca Digital

**Data:** 30/10/2025  
**Responsável:** Gustavo Bastos  

---

## Funcionalidades Testadas

### 1. Listar Documentos
- **Descrição:** Lista todos os arquivos da pasta `docs/` agrupados por tipo.  
- **Resultado Esperado:** Todos os arquivos são exibidos corretamente com suas extensões.  
- **Resultado Obtido:** ✅ Funcionou corretamente, exibindo PDFs, ePUBs, DOCX, etc.

---

### 2. Adicionar Documento
- **Descrição:** Adiciona novo documento com validação de título e ano.  
- **Resultado Esperado:** Não aceita título vazio nem ano inválido; arquivo é copiado para `docs/`.  
- **Resultado Obtido:** ✅ Validação funcionando; documento adicionado com sucesso.

---

### 3. Renomear Documento
- **Descrição:** Permite renomear um ou múltiplos documentos de uma vez.  
- **Resultado Esperado:** Documentos renomeados seguindo padrão `titulo_tipo_ano.ext`; evita sobrescrita.  
- **Resultado Obtido:** ✅ Funcionou perfeitamente, inclusive múltiplos arquivos.

---

### 4. Remover Documento
- **Descrição:** Remove documentos, movendo-os para a pasta `trash/`.  
- **Resultado Esperado:** Documento removido da pasta principal e salvo na lixeira; confirmação antes da ação.  
- **Resultado Obtido:** ✅ Funcionou corretamente; confirmações exibidas e arquivos movidos.

---

### 5. Restaurar Documento
- **Descrição:** Restaura documentos da lixeira para `docs/`.  
- **Resultado Esperado:** Documento restaurado corretamente; evita sobrescrita de arquivos existentes.  
- **Resultado Obtido:** ✅ Funcionou corretamente, incluindo verificação de conflitos.

---

### 6. Cores no Terminal
- **Descrição:** Mensagens de erro, aviso e sucesso diferenciadas por cores.  
- **Resultado Esperado:** Cores aplicadas corretamente.  
- **Resultado Obtido:** ✅ Todas as mensagens exibidas com cores, melhorando a experiência.

---

## Conclusão
O sistema está funcionando com excelência, todas as funcionalidades implementadas estão testadas e validadas. A lixeira, validações e renomeação múltipla melhoram significativamente a gestão dos documentos digitais.
