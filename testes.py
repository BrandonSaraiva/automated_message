import pyautogui
import time

time.sleep(3)

# Obter as coordenadas do mouse
x, y = pyautogui.position()

print(f"({x}, {y})")