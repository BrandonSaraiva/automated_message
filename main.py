# importações das bibliotecas e funções
from datetime import datetime
from funcoes.pyauto import selecUser
import threading
import time
from funcoes.shopee import shopeeDiary
from funcoes.envio import enviar_mensagem
from selenium.common.exceptions import WebDriverException
import colorama
from colorama import Fore, Style


def run_at_specific_times():
    try:
        colorama.init()
        hoje = datetime.now().date()  # Obtém a data atual
        foi_todos = False  # Boleano para controlar a impressão de "ENVIEI MSG PARA TODOS NA LISTA"
        shopi = False

        pessoas = int(
            input("\nQuantas pessoas você quer enviar mensagens (0 para enviar nenhuma e deixar só a funcionalidade da shopee rodando)?:  "))  # Pergunta o número de pessoas para enviar mensagens

        mensagens = []
        if pessoas > 0:
            escolha = input(
                "\nAs mensagens devem ser enviadas hoje? (s/n): ")  # Pergunta se as mensagens devem ser enviadas hoje
            for i in range(pessoas):
                nome = input(f"\nDigite o nome da pessoa {i + 1}: ")  # Pergunta o nome da pessoa
                mensagem = input(f"\nDigite a mensagem para a pessoa {i + 1}: ")  # Pergunta a mensagem para a pessoa
                hora = int(input(
                    f"\nDigite a hora que deseja enviar a mensagem para a pessoa {i + 1}: "))  # Pergunta a hora para enviar a mensagem
                minuto = int(input(
                    f"\nDigite o minuto que deseja enviar a mensagem para a pessoa {i + 1}: "))  # Pergunta o minuto para enviar a mensagem
                mensagens.append((nome, mensagem, hora, minuto))  # Adiciona as informações da mensagem à lista de mensagens

            print("\nTudo certo! Irei enviar suas mensagens nesses horarios!")  # Confirmação das mensagens a serem enviadas

            if escolha.lower() == 'n':
                dia_especifico = int(input("\nDigite o dia específico que a mensagem será enviada: "))  # Pergunta o dia específico para enviar as mensagens
                data_especifica = datetime(hoje.year, hoje.month, dia_especifico).date()  # Cria uma data específica
                print("\nTudo certo, agora só aguardar!")
                while hoje < data_especifica:
                    hoje = datetime.now().date()
                    current_time = time.localtime()
                    hour = current_time.tm_hour

                    # Caso seja 22 horas e ja nao tenha pegado as moedas
                    if hour == 22 and not shopi:
                        try:
                            t = threading.Thread(
                                target=selecUser)  # Cria uma thread para executar a função selecUser em paralelo, a select user clica no usuario do chrome
                            t.start()  # Inicia a execução da thread
                            shopeeDiary()  # Executa a função shopeeDiary
                            shopi = True
                        except WebDriverException as e:
                            print(
                                Style.BRIGHT + "Erro!!Para o código funcionar, você não pode ter outra janela do Google Chrome aberta.")
                            print(Style.BRIGHT + "Por favor, feche todas as janelas do Google Chrome e tente novamente.")
                            return
                    time.sleep(60)  # Espera 1 minuto antes de verificar novamente

        counter = 0  # Contador para acompanhar quantas mensagens foram enviadas
        print("\nAgora só aguardar!")
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
                    print(Style.BRIGHT + "\nTERMINEI DE ENVIAR AS MSGS PARA TODOS" + Style.RESET_ALL + " 😀")  # Imprime uma mensagem quando todas as mensagens forem enviadas
                    foi_todos = True

            # Caso seja 22 horas e ja nao tenha pegado as moedas
            if hour == 22 and not shopi:
                try:
                    t = threading.Thread(
                        target=selecUser)  # Cria uma thread para executar a função selecUser em paralelo, a select user clica no usuario do chrome
                    t.start()  # Inicia a execução da thread
                    conferir_shopee = shopeeDiary()  # Executa a função shopeeDiary
                    if conferir_shopee:
                        shopi = True
                except WebDriverException as e:
                    print(Style.BRIGHT + "\nProvavelmente ainda não foi liberada as moedas")
                    print(
                        Style.BRIGHT + "\nErro!!Para o código funcionar, você não pode ter outra janela do Google Chrome aberta.")
                    print(Style.BRIGHT + "Por favor, feche todas as janelas do Google Chrome e tente novamente.")
                    return

            time.sleep(31)  # Aguarda 31 segundos antes de verificar novamente
    except WebDriverException as e:
        print(
            Style.BRIGHT + "\nErro!!Para o código funcionar, você não pode ter outra janela do Google Chrome aberta.")
        print(Style.BRIGHT + "Por favor, feche todas as janelas do Google Chrome e tente novamente.")
        return

if __name__ == '__main__':
    while True:
        run_at_specific_times()

