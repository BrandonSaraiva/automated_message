# importações das bibliotecas e funções
from funcoes.wts import webWts
import time
from funcoes.pyauto import selecUser
import threading

def enviar_mensagem(nome, mensagem, minute):
    current_time = time.localtime()
    # Obtém o tempo atual usando a função localtime do módulo time e armazena na variável current_time

    hour = current_time.tm_hour
    # Extrai a hora atual

    hora_envio = mensagem[2]
    # Extrai a hora de envio da mensagem a partir do terceiro elemento da lista mensagem e armazena em hora_envio

    minuto_envio = mensagem[3]
    # Extrai o minuto de envio da mensagem a partir do quarto elemento da lista mensagem e armazena em minuto_envio

    if hour == hora_envio and minute == minuto_envio:
        # Verifica se a hora atual é igual à hora de envio e se o minuto atual é igual ao minuto de envio

        t = threading.Thread(target=selecUser)
        # Threading para clicar no usuario do chrome

        t.start()
        # Inicia a execução da thread t

        webWts(nome, mensagem[1])
        # Chama a função webWts, passando o nome e a mensagem como argumentos, para abrir o WTS e enviar a mensagem

        t.join()
        # Aguarda a conclusão da execução da thread t

        return True
        # Retorna True se a mensagem for enviada com sucesso

    return False
    # Retorna False se a mensagem não for enviada nesta execução