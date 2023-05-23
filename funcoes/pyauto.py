import time
import pyautogui

def selecUser():
    # Aguardando um tempo para permitir que o navegador seja aberto
    time.sleep(5)

    # Movendo o mouse para a posição desejada e clicando
    pyautogui.moveTo(750, 615)
    pyautogui.click()