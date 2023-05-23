from funcoes.wts import webWts
import time
from funcoes.pyauto import selecUser
import threading

def enviar_mensagem(nome, mensagem, minute):
    current_time = time.localtime()
    hour = current_time.tm_hour
    hora_envio = mensagem[2]
    minuto_envio = mensagem[3]

    if hour == hora_envio and minute == minuto_envio:
        t = threading.Thread(target=selecUser)
        t.start()
        webWts(nome, mensagem[1])
        t.join()  # Aguarda a conclusão do envio da mensagem

        return True  # Retorna True se a mensagem for enviada com sucesso

    return False  # Retorna False se a mensagem não foi enviada nesta execução
