# importações das bibliotecas e funções
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pyperclip
from funcoes.momento_atual import hora_atual

def webWts(nome, texto):
    try:
    # Obtendo o nome de usuário do sistema
        username = getpass.getuser()

        # Obtendo as opções do navegador
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\")

        # Inicializando o driver do navegador
        driver = webdriver.Chrome(options=options)

        # Abrindo o WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Aguardando um tempo para o carregamento da página
        time.sleep(20)

        # Localizando o campo de pesquisa e digitando o nome do contato/grupo
        search_box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
        search_box.send_keys(nome)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)
        # Clicando pra abrir o chat
        compose_box = driver.find_element(By.CSS_SELECTOR, "div[data-testid='conversation-compose-box-input']")
        compose_box.click()

        # Clicando pra digitar o texto
        element = driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]')
        element.click()

        # Definindo o valor do campo de texto usando emojis
        emoji_text = texto

        # Copia o texto com emojis para a área de transferência
        pyperclip.copy(emoji_text)

        # Cola o texto na caixa de texto usando as teclas de atalho Ctrl+V
        element.send_keys(Keys.CONTROL, 'v')

        time.sleep(1)

        # Clicando no botao de enviar
        send_button = driver.find_element(By.CSS_SELECTOR,'[data-testid="compose-btn-send"]')
        send_button.click()

        print(f'\nEnviei a mensagem para {nome} agora, são: {hora_atual()}')
        time.sleep(3)

        driver.quit()


    except NoSuchElementException:
        print("\n!Erro ao achar algum elemento na pagina!")

