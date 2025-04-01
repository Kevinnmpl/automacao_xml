from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import central
import pandas as pd
import download_arq
import time

driver = webdriver.Chrome()

site = driver.get("https://www.centraldaescola.com.br")

driver.maximize_window()

# seleciona tipo de usuário
def tipoPerfil(idPerfil, perfil):
    tipo_de_perfil = driver.find_element(By.ID, idPerfil)
    tipo_de_perfil.click()
    tipo_de_perfil.send_keys(perfil, Keys.ENTER)

# preenche o usuário e a senha
def preencherLogin(idUsuario, idSenha, usuario, senha):
    input_de_usuario = driver.find_element(By.ID, idUsuario)
    input_de_usuario.send_keys(usuario)
    input_de_senha = driver.find_element(By.ID, idSenha)
    input_de_senha.send_keys(senha)
    time.sleep(15)

# url da página de carga de xml
def urlFinanceiro(url):
    driver.get(url)

# lê csv das escolas e mudar id na url
def mudarDeEscola(csv, url):
    
    escolas = pd.read_csv(csv)

    for _, linha in escolas.iterrows():
        id = linha["id_escola"]
        url_base = f"{url}{id}"
        
        driver.get(url_base)
        time.sleep(4)

if __name__ == '__main__':

    tipo_perfil = tipoPerfil('Adm')

    login = preencherLogin(central['campo_usuario'], 
                           central['campo_senha'], 
                           central['usuario'], 
                           central['senha'])

    url_xml = central['url_financeiro']

    escola = mudarDeEscola('escolas_teste.csv', url_xml)





# # ultimo arquivo xml
# ultimo_arquivo_xml = download_arq.ultimo_arquivo

# # selecionar arquivo
# escolher_arquivo = navegador.find_element(By.ID, "file")
# escolher_arquivo.send_keys(ultimo_arquivo_xml)

# # enviar arquivo
# botao_enviar = navegador.find_element(By.ID, "btnEnviar")
# botao_enviar.click

# time.sleep(4)







# IDEIAS
# colocar o link do central + o id - navegador.get() em um loop com o mesmo link e so muda o id final da escola
# pegar no athena com o nome da escola
# ver forma de pegar ultimo arquivo baixado e colocar no central

# pegar os ids corretos das escolas - pedido pra larissa