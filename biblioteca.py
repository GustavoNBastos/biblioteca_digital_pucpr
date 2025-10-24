import os

# Caminho da pasta docs
PASTA_DOCS = "docs"

def listar_documentos():
    if not os.path.exists(PASTA_DOCS):
        print(f"\nA pasta '{PASTA_DOCS}' não existe. Crie-a para adicionar documentos.")
        return

    arquivos = os.listdir(PASTA_DOCS)
    if not arquivos:
        print("\nNão há documentos na pasta.")
        return

    # Organizar arquivos por extensão
    documentos_por_tipo = {}
    for arquivo in arquivos:
        if os.path.isfile(os.path.join(PASTA_DOCS, arquivo)):
            extensao = os.path.splitext(arquivo)[1].lower()
            if extensao not in documentos_por_tipo:
                documentos_por_tipo[extensao] = []
            documentos_por_tipo[extensao].append(arquivo)

    print("\n=== Documentos na Biblioteca ===")
    for tipo, lista in documentos_por_tipo.items():
        print(f"\nTipo {tipo}:")
        for doc in lista:
            print(f" - {doc}")

def adicionar_documento():
    print("\n[Em desenvolvimento] - Função para adicionar documentos.")

def renomear_documento():
    print("\n[Em desenvolvimento] - Função para renomear documentos.")

def remover_documento():
    print("\n[Em desenvolvimento] - Função para remover documentos.")
