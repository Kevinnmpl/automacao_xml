from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import athena

# inicializa o driver (google)
driver = webdriver.Chrome()

# roda a função do login
navegador = driver.get("https://www.athenaweb.com.br")

# maximiza a tela
# navegador.maximize_window()

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

if __name__ == '__main__':

    login = preencherLogin(athena['campo_usuario'], athena['campo_senha'], athena['usuario'], athena['senha'])

    campo_escola = selecionarCampoEscola('select2-selection__rendered')

    nome_escola = digitarEscola('select2-search__field', 'Arte de Crescer')

    botao_selecionar = pressionarBotaoSelecionar('btn-selectCedente')

    url_receber = urlModuloReceber('https://www.athenaweb.com.br/receber/manutencao')
    
    tipo_xml = selecionarTipoXml('tipo_select', 'boletos')
    
    geracao = gerarXml('btnGerar')
