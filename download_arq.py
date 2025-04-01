import os
import time
import glob

# PEGA O ULTIMO ARQUIVO BAIXADO

pasta_downloads = os.path.expanduser("~\Downloads")

def pegar_ultimo_arquivo(pasta_downloads):
    # Aguarda um tempo para garantir que o download foi concluído
    time.sleep(3)

    # lista todos os arquivos da pasta de downloads
    arquivos = glob.glob(os.path.join(pasta_downloads, "*.xml"))

    if not arquivos:
        return None  # Nenhum arquivo encontrado

    # Pega o arquivo mais recente
    arquivo_mais_recente = max(arquivos, key=os.path.getctime)
    return arquivo_mais_recente

# Obter o último arquivo baixado
ultimo_arquivo = pegar_ultimo_arquivo(pasta_downloads)

if ultimo_arquivo:
    print(f"Último arquivo baixado: {ultimo_arquivo}")
else:
    print("Nenhum arquivo encontrado!")


# caminho para os downloads
# pasta_downloads = os.path.expanduser("~/Downloads")

# # pegar último arquivo baixado
# ultimo_arquivo = download_arq.pegar_ultimo_arquivo(pasta_downloads)

# if ultimo_arquivo:
#     print(f"Último arquivo baixado: {ultimo_arquivo}")
# else:
#     print("Nenhum arquivo encontrado!")

# CODIGO PARA URL PERSONALIZADA

# Carregar os dados do CSV
# escolas = pd.read_csv('escolas.csv')