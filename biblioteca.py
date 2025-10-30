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
def renomear_documento():
    """Renomeia um documento existente com base em novo título e ano."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)

    if not arquivos:
        print("\n📂 Nenhum documento encontrado na biblioteca.")
        return

    print("\n=== Documentos Disponíveis ===")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    nome_atual = input("\nDigite o nome exato do documento que deseja renomear (com extensão): ").strip()
    caminho_atual = os.path.join(PASTA_DOCS, nome_atual)

    if not os.path.exists(caminho_atual):
        print("❌ Documento não encontrado. Verifique o nome e tente novamente.")
        return

    novo_titulo = input("Digite o novo título do documento: ").strip()
    novo_ano = input("Digite o novo ano de publicação: ").strip()

    # Detecta o tipo automaticamente pela extensão
    _, extensao = os.path.splitext(nome_atual)
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

    # Novo nome padronizado
    novo_nome = f"{novo_titulo.replace(' ', '_')}_{tipo}_{novo_ano}{extensao}"
    caminho_novo = os.path.join(PASTA_DOCS, novo_nome)

    # Evita sobrescrita acidental
    if os.path.exists(caminho_novo):
        print(f"⚠️ Já existe um arquivo chamado '{novo_nome}'. Operação cancelada.")
        return

    os.rename(caminho_atual, caminho_novo)
    print(f"✅ Documento renomeado com sucesso para '{novo_nome}'.")


def remover_documento():
    """Remove um documento existente da pasta docs."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)

    if not arquivos:
        print("\n📂 Nenhum documento encontrado na biblioteca.")
        return

    print("\n=== Documentos Disponíveis ===")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    nome_remover = input("\nDigite o nome exato do documento que deseja remover (com extensão): ").strip()
    caminho_remover = os.path.join(PASTA_DOCS, nome_remover)

    if not os.path.exists(caminho_remover):
        print("❌ Documento não encontrado. Verifique o nome e tente novamente.")
        return

    confirmacao = input(f"⚠️ Tem certeza que deseja remover '{nome_remover}'? (s/n): ").strip().lower()
    if confirmacao != 's':
        print("❌ Operação cancelada pelo usuário.")
        return

    os.remove(caminho_remover)
    print(f"✅ Documento '{nome_remover}' removido com sucesso.")
