# importações das bibliotecas e funções
from selenium import webdriver
import time
import getpass
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from funcoes.momento_atual import hora_atual

def shopeeDiary():
    try:
        # Obtendo o nome de usuário do sistema
        username = getpass.getuser()

        # Obtendo as opções do navegador
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\")

        # Inicializando o driver do navegador
        driver = webdriver.Chrome(options=options)

        # Abrindo o site
        driver.get("https://shopee.com.br/shopee-coins/")
        time.sleep(5)

        # LOcalizando o botao e clicando nele 3 vezes para ter ctz q foi
        for c in range(3):
            button = driver.find_element(By.CSS_SELECTOR, 'button.pcmall-dailycheckin_3u8jig')
            button.click()
            time.sleep(1)

        print(f"\nTentei clicar no botao da shopee agora as {hora_atual()}")

        driver.quit()
    except NoSuchElementException:
        print("\n!Erro ao achar algum elemento na pagina!")
