import os
import shutil

PASTA_DOCS = "docs"

def garantir_pasta():
    """Garante que a pasta de documentos exista."""
    if not os.path.exists(PASTA_DOCS):
        os.makedirs(PASTA_DOCS)

def listar_documentos():
    """Lista os documentos existentes na pasta docs, agrupados por tipo."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)

    if not arquivos:
        print("\n📂 Não há documentos na pasta.")
        return

    documentos_por_tipo = {}
    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DOCS, arquivo)
        if os.path.isfile(caminho):
            extensao = os.path.splitext(arquivo)[1].lower() or "[sem extensão]"
            documentos_por_tipo.setdefault(extensao, []).append(arquivo)

    print("\n=== Documentos na Biblioteca ===")
    for tipo, lista in documentos_por_tipo.items():
        print(f"\nTipo {tipo}:")
        for doc in lista:
            print(f" - {doc}")

def adicionar_documento():
    """Adiciona um novo documento informando apenas título e ano; o tipo é detectado automaticamente."""
    garantir_pasta()

    print("\n=== Adicionar Novo Documento ===")
    titulo = input("Digite o título do documento: ").strip()
    ano = input("Digite o ano de publicação: ").strip()
    caminho_arquivo = input("Arraste o arquivo aqui e pressione ENTER: ").strip().strip('"')

    if not os.path.isfile(caminho_arquivo):
        print("❌ Arquivo não encontrado. Verifique o caminho informado.")
        return

    # Detectar extensão e tipo automaticamente
    _, extensao = os.path.splitext(caminho_arquivo)
    extensao = extensao.lower()

    tipos = {
        ".pdf": "artigo",
        ".docx": "relatório",
        ".pptx": "apresentação",
        ".jpg": "imagem",
        ".jpeg": "imagem",
        ".png": "imagem",
        ".txt": "texto"
    }
    tipo = tipos.get(extensao, "outro")

    # Criar nome padronizado
    nome_arquivo = f"{titulo.replace(' ', '_')}_{tipo}_{ano}{extensao}"
    destino = os.path.join(PASTA_DOCS, nome_arquivo)

    # Copiar o arquivo original para a pasta docs
    shutil.copy2(caminho_arquivo, destino)

    print(f"✅ Documento '{nome_arquivo}' adicionado com sucesso à biblioteca!")
    print(f"📂 Caminho: {os.path.abspath(destino)}")
