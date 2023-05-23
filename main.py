# importações das bibliotecas e funções
from datetime import datetime
from funcoes.pyauto import selecUser
import threading
import time
from funcoes.shopee import shopeeDiary
from funcoes.envio import enviar_mensagem
from selenium.common.exceptions import WebDriverException

def run_at_specific_times():
    hoje = datetime.now().date()  # Obtém a data atual
    escolha = input("\nAs mensagens devem ser enviadas hoje? (s/n): ")  # Pergunta se as mensagens devem ser enviadas hoje
    if escolha.lower() == 'n':
        dia_especifico = int(input("\nDigite o dia específico: "))  # Pergunta o dia específico para enviar as mensagens
        data_especifica = datetime(hoje.year, hoje.month, dia_especifico).date()  # Cria uma data específica
        while hoje < data_especifica:
            hoje = datetime.now().date()
            time.sleep(60)  # Espera 1 minuto antes de verificar novamente

    pessoas = int(input("\nQuantas pessoas você quer enviar mensagens?: "))  # Pergunta o número de pessoas para enviar mensagens

    mensagens = []
    for i in range(pessoas):
        nome = input(f"\nDigite o nome da pessoa {i + 1}: ")  # Pergunta o nome da pessoa
        mensagem = input(f"\nDigite a mensagem para a pessoa {i + 1}: ")  # Pergunta a mensagem para a pessoa
        hora = int(input(f"\nDigite a hora que deseja enviar a mensagem para a pessoa {i + 1}: "))  # Pergunta a hora para enviar a mensagem
        minuto = int(input(f"\nDigite o minuto que deseja enviar a mensagem para a pessoa {i + 1}: "))  # Pergunta o minuto para enviar a mensagem
        mensagens.append((nome, mensagem, hora, minuto))  # Adiciona as informações da mensagem à lista de mensagens

    print("\nTudo certo! Irei enviar suas mensagens!")  # Confirmação das mensagens a serem enviadas

    foi_todos = False  # Boleano para controlar a impressão de "ENVIEI MSG PARA TODOS NA LISTA"
    counter = 0  # Contador para acompanhar quantas mensagens foram enviadas

    while True:
        current_time = time.localtime()  # Obtém a hora atual
        hour = current_time.tm_hour  # Obtém a hora atual
        minute = current_time.tm_min  # Obtém o minuto atual

        for mensagem in mensagens:
            try:
                enviado = enviar_mensagem(mensagem[0], mensagem, minute)  # Envia a mensagem para a pessoa
                if enviado:
                    counter += 1  # Incrementa o contador se a mensagem for enviada com sucesso
            except WebDriverException as e:
                print("\nErro: Para o código funcionar, você não pode ter outra janela do Google Chrome aberta.")
                print("Por favor, feche todas as janelas do Google Chrome e tente novamente.")
                return

            # Caso tenha enviado todas as msgs
            if counter == len(mensagens) and not foi_todos:
                print(
                    "\n\033[1mTERMINEI DE ENVIAR AS MSGS PARA TODOS\033[😀")  # Imprime uma mensagem quando todas as mensagens forem enviadas
                foi_todos = True

            # Caso seja 22 horas e ja nao tenha pegado as moedas
            if hour == 22 and not foi_todos:
                try:
                    t = threading.Thread(
                        target=selecUser)  # Cria uma thread para executar a função selecUser em paralelo, a select user clica no usuario do chrome
                    t.start()  # Inicia a execução da thread
                    shopeeDiary()  # Executa a função shopeeDiary
                    foi_todos = True
                except WebDriverException as e:
                    print(
                        "\n\033[1mErro!!\033[: Para o código funcionar, você não pode ter outra janela do Google Chrome aberta.")
                    print("Por favor, feche todas as janelas do Google Chrome e tente novamente.")
                    return

            time.sleep(31)  # Aguarda 31 segundos antes de verificar novamente

if __name__ == '__main__':
    run_at_specific_times()

