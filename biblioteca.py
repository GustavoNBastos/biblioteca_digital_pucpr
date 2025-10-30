import os
import shutil

PASTA_DOCS = "docs"
PASTA_TRASH = "trash"

# ANSI colors
class Cores:
    SUCESSO = '\033[92m'   # Verde
    AVISO = '\033[93m'     # Amarelo
    ERRO = '\033[91m'      # Vermelho
    INFO = '\033[94m'      # Azul
    RESET = '\033[0m'

def garantir_pasta():
    """Garante que as pastas de documentos e lixeira existam."""
    for pasta in [PASTA_DOCS, PASTA_TRASH]:
        if not os.path.exists(pasta):
            os.makedirs(pasta)

def listar_documentos():
    """Lista documentos agrupados por tipo."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)
    if not arquivos:
        print(f"\n{Cores.INFO}📂 Não há documentos na pasta.{Cores.RESET}")
        return

    documentos_por_tipo = {}
    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DOCS, arquivo)
        if os.path.isfile(caminho):
            extensao = os.path.splitext(arquivo)[1].lower() or "[sem extensão]"
            documentos_por_tipo.setdefault(extensao, []).append(arquivo)

    print(f"\n{Cores.INFO}=== Documentos na Biblioteca ==={Cores.RESET}")
    for tipo, lista in documentos_por_tipo.items():
        print(f"\nTipo {tipo}:")
        for doc in lista:
            print(f" - {doc}")

def validar_titulo_ano(titulo, ano):
    if not titulo.strip():
        print(f"{Cores.ERRO}❌ Título não pode ser vazio.{Cores.RESET}")
        return False
    if not ano.strip() or not ano.isdigit():
        print(f"{Cores.ERRO}❌ Ano inválido. Digite apenas números.{Cores.RESET}")
        return False
    return True

def adicionar_documento():
    """Adiciona um novo documento com validação de título e ano."""
    garantir_pasta()
    print(f"\n{Cores.INFO}=== Adicionar Novo Documento ==={Cores.RESET}")
    titulo = input("Digite o título do documento: ").strip()
    ano = input("Digite o ano de publicação: ").strip()
    if not validar_titulo_ano(titulo, ano):
        return
    caminho_arquivo = input("Arraste o arquivo aqui e pressione ENTER: ").strip().strip('"')

    if not os.path.isfile(caminho_arquivo):
        print(f"{Cores.ERRO}❌ Arquivo não encontrado.{Cores.RESET}")
        return

    _, extensao = os.path.splitext(caminho_arquivo)
    extensao = extensao.lower()
    tipos = {".pdf": "artigo", ".docx": "relatório", ".pptx": "apresentação",
             ".jpg": "imagem", ".jpeg": "imagem", ".png": "imagem", ".txt": "texto"}
    tipo = tipos.get(extensao, "outro")

    nome_arquivo = f"{titulo.replace(' ', '_')}_{tipo}_{ano}{extensao}"
    destino = os.path.join(PASTA_DOCS, nome_arquivo)
    shutil.copy2(caminho_arquivo, destino)
    print(f"{Cores.SUCESSO}✅ Documento '{nome_arquivo}' adicionado com sucesso!{Cores.RESET}")
    print(f"📂 Caminho: {os.path.abspath(destino)}")

def renomear_documento():
    """Renomeia um ou múltiplos documentos existentes."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)
    if not arquivos:
        print(f"\n{Cores.INFO}📂 Nenhum documento encontrado.{Cores.RESET}")
        return

    print(f"\n{Cores.INFO}=== Documentos Disponíveis ==={Cores.RESET}")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    indices = input("\nDigite os números dos documentos a renomear separados por vírgula: ").split(',')
    try:
        indices = [int(i.strip())-1 for i in indices]
    except ValueError:
        print(f"{Cores.ERRO}❌ Entrada inválida.{Cores.RESET}")
        return

    for i in indices:
        if i < 0 or i >= len(arquivos):
            print(f"{Cores.AVISO}⚠️ Documento {i+1} inválido, pulando.{Cores.RESET}")
            continue

        nome_atual = arquivos[i]
        caminho_atual = os.path.join(PASTA_DOCS, nome_atual)
        novo_titulo = input(f"Digite o novo título para '{nome_atual}': ").strip()
        novo_ano = input("Digite o novo ano de publicação: ").strip()
        if not validar_titulo_ano(novo_titulo, novo_ano):
            continue

        _, extensao = os.path.splitext(nome_atual)
        extensao = extensao.lower()
        tipos = {".pdf": "artigo", ".docx": "relatório", ".pptx": "apresentação",
                 ".jpg": "imagem", ".jpeg": "imagem", ".png": "imagem", ".txt": "texto"}
        tipo = tipos.get(extensao, "outro")
        novo_nome = f"{novo_titulo.replace(' ', '_')}_{tipo}_{novo_ano}{extensao}"
        caminho_novo = os.path.join(PASTA_DOCS, novo_nome)
        if os.path.exists(caminho_novo):
            print(f"{Cores.AVISO}⚠️ Arquivo '{novo_nome}' já existe, pulando.{Cores.RESET}")
            continue
        os.rename(caminho_atual, caminho_novo)
        print(f"{Cores.SUCESSO}✅ Documento renomeado para '{novo_nome}'{Cores.RESET}")

def remover_documento():
    """Remove documento movendo para lixeira temporária."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_DOCS)
    if not arquivos:
        print(f"\n{Cores.INFO}📂 Nenhum documento encontrado.{Cores.RESET}")
        return

    print(f"\n{Cores.INFO}=== Documentos Disponíveis ==={Cores.RESET}")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    indices = input("\nDigite os números dos documentos a remover separados por vírgula: ").split(',')
    try:
        indices = [int(i.strip())-1 for i in indices]
    except ValueError:
        print(f"{Cores.ERRO}❌ Entrada inválida.{Cores.RESET}")
        return

    for i in indices:
        if i < 0 or i >= len(arquivos):
            print(f"{Cores.AVISO}⚠️ Documento {i+1} inválido, pulando.{Cores.RESET}")
            continue
        nome_remover = arquivos[i]
        caminho_remover = os.path.join(PASTA_DOCS, nome_remover)
        confirmacao = input(f"⚠️ Tem certeza que deseja remover '{nome_remover}'? (s/n): ").strip().lower()
        if confirmacao != 's':
            print(f"{Cores.AVISO}❌ Operação cancelada.{Cores.RESET}")
            continue
        destino_lixeira = os.path.join(PASTA_TRASH, nome_remover)
        shutil.move(caminho_remover, destino_lixeira)
        print(f"{Cores.SUCESSO}✅ Documento '{nome_remover}' movido para a lixeira.{Cores.RESET}")

def restaurar_documento():
    """Restaura documentos da lixeira para a pasta principal."""
    garantir_pasta()
    arquivos = os.listdir(PASTA_TRASH)
    if not arquivos:
        print(f"\n{Cores.INFO}📂 Lixeira vazia.{Cores.RESET}")
        return

    print(f"\n{Cores.INFO}=== Documentos na Lixeira ==={Cores.RESET}")
    for i, arquivo in enumerate(arquivos, start=1):
        print(f"{i}. {arquivo}")

    indices = input("\nDigite os números dos documentos a restaurar separados por vírgula: ").split(',')
    try:
        indices = [int(i.strip())-1 for i in indices]
    except ValueError:
        print(f"{Cores.ERRO}❌ Entrada inválida.{Cores.RESET}")
        return

    for i in indices:
        if i < 0 or i >= len(arquivos):
            print(f"{Cores.AVISO}⚠️ Documento {i+1} inválido, pulando.{Cores.RESET}")
            continue
        nome_restaurar = arquivos[i]
        caminho_trash = os.path.join(PASTA_TRASH, nome_restaurar)
        destino = os.path.join(PASTA_DOCS, nome_restaurar)
        if os.path.exists(destino):
            print(f"{Cores.AVISO}⚠️ Arquivo '{nome_restaurar}' já existe, pulando.{Cores.RESET}")
            continue
        shutil.move(caminho_trash, destino)
        print(f"{Cores.SUCESSO}✅ Documento '{nome_restaurar}' restaurado com sucesso.{Cores.RESET}")
