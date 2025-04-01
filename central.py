from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import download_arq
import time

navegador = webdriver.Chrome()

site = navegador.get("https://www.centraldaescola.com.br")

# Maximiza a tela
# maximizar_tela = navegador.maximize_window()

# selecionar tipo de usuário
tipo_de_perfil = navegador.find_element(By.ID, "perfil")
tipo_de_perfil.click()
tipo_de_perfil.send_keys("Adm", Keys.ENTER)

# Preencher o usuário e a senha
input_de_usuario = navegador.find_element(By.ID, "login")
input_de_usuario.send_keys("adelia.logon")
input_de_senha = navegador.find_element(By.ID, "senha")
input_de_senha.send_keys("123mudar")

# Base da URL
url_base = navegador.get("https://www.centraldaescola.com.br/administrador/importacoes/financeiro_xml/165")

# # ler csv das escolas
# escolas = pd.read_csv("escolas.csv")

# # adicionar id da escola no final da url
# for _, linha in escolas.iterrows():
#     # Gerar a URL para cada escola com o ID
#     id = linha["id_escola"]
#     url = f"{url_base}{id}"
    
#     navegador.get(url)
#     time.sleep(4)

# ultimo arquivo xml
ultimo_arquivo_xml = download_arq.ultimo_arquivo

# selecionar arquivo
escolher_arquivo = navegador.find_element(By.ID, "file")
escolher_arquivo.send_keys(ultimo_arquivo_xml)

# enviar arquivo
botao_enviar = navegador.find_element(By.ID, "btnEnviar")
botao_enviar.click

time.sleep(4)







# IDEIAS
# colocar o link do central + o id - navegador.get() em um loop com o mesmo link e so muda o id final da escola
# pegar no athena com o nome da escola
# ver forma de pegar ultimo arquivo baixado e colocar no central

# pegar os ids corretos das escolas - pedido pra larissa