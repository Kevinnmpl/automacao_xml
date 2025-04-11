import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import athena

# carrega lista com os nomes das escolas
df = pd.read_csv("nome_escolas.csv")
nomes_escolas = df["nomefantasia"]

# inicializa o driver (google)
driver = webdriver.ChromeOptions()

# define o diretório do perfil do usuário no chrome
driver.add_argument(r'--user-data-dir=C:\Users\Galalaucio2\AppData\Local\Google\Chrome\User Data')
driver.add_argument('--profile-directory=Default') # pefil desejado

# inicializa o chrome com o perfil selecionado
driver = webdriver.Chrome(options=driver)

# roda a função do login
navegador = driver.get("https://www.athenaweb.com.br")

# preenche o usuário e a senha
def preencherLogin(classeUsuario, classeSenha, usuario, senha):
    input_de_usuario = driver.find_element(By.NAME, classeUsuario)
    input_de_usuario.send_keys(usuario)
    input_de_senha = driver.find_element(By.NAME, classeSenha)
    input_de_senha.send_keys(senha)
    time.sleep(10)
    input_de_usuario.submit()

# seleciona campo para digitar escola
def selecionarCampoEscola(classe):
    time.sleep(4)
    selecionar_campo_escola = driver.find_element(By.CLASS_NAME, classe)
    selecionar_campo_escola.click()

# digita escola
def digitarEscola(classe, nomeEscola):
    digitar_escola = driver.find_element(By.CLASS_NAME, classe)
    digitar_escola.send_keys(nomeEscola, Keys.ENTER)
    time.sleep(2)

# pressiona o botao de selecionar após escolher escola
def pressionarBotaoSelecionar(id):
    botao_selecionar = driver.find_element(By.ID, id)
    botao_selecionar.send_keys(Keys.ENTER)

# abre o modulo receber pela url
def urlModuloReceber(url):
    time.sleep(4)
    driver.get(url)
    
# seleciona o tipo do xml (alunos, boletos)
def selecionarTipoXml(id, tipo):
    tipo_boleto = driver.find_element(By.ID, id)
    tipo_boleto.send_keys(tipo)
    
# gera xml
def gerarXml(id):
    botao_gerar = driver.find_element(By.ID, id)
    botao_gerar.click()
    time.sleep(20)

# trocar a escola e confirmar
def trocarEscola_e_confirmartroca(id_trocar, id_confirmar):
    botao_trocar = driver.find_element(By.ID, id_trocar)
    time.sleep(2)
    botao_trocar.click()
    time.sleep(2)
    botao_confirmar = driver.find_element(By.ID, id_confirmar)
    time.sleep(2)
    botao_confirmar.click()
     

if __name__ == '__main__':

    login = preencherLogin(athena['campo_usuario'], athena['campo_senha'], athena['usuario'], athena['senha'])

    for nome_escola in nomes_escolas:

        driver.get("https://www.athenaweb.com.br")  # retorna à página inicial
        
        try:
            selecionarCampoEscola('select2-selection__rendered') # seleciona o campo de escola
        except:
            trocarEscola_e_confirmartroca('btn-trocar-escola', 'confirma-troca') # trocar a escola e confirmar
            selecionarCampoEscola('select2-selection__rendered') # seleciona o campo de escola

        digitarEscola('select2-search__field', nome_escola)  # digita o nome da escola
        pressionarBotaoSelecionar('btn-selectCedente')  # seleciona a escola

        urlModuloReceber('https://www.athenaweb.com.br/receber/manutencao')  # abre o módulo de receber
        selecionarTipoXml('tipo_select', 'boletos')  # seleciona o tipo de XML
        gerarXml('btnGerar')  # gera o XML
