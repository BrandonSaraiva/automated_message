from datetime import datetime, timedelta
from funcoes.pyauto import selecUser
import threading
import time
from funcoes.shopee import shopeeDiary
from funcoes.envio import enviar_mensagem

def run_at_specific_times():
    hoje = datetime.now().date()
    escolha = input("\nAs mensagens devem ser enviadas hoje? (s/n): ")
    if escolha.lower() == 'n':
        dia_especifico = int(input("\nDigite o dia específico: "))
        data_especifica = datetime(hoje.year, hoje.month, dia_especifico).date()
        while hoje < data_especifica:
            hoje = datetime.now().date()
            time.sleep(60)  # Espera 1 minuto antes de verificar novamente

    # Resto do código continua aqui...

    pessoas = int(input("\nDigite o número de pessoas para enviar a mensagem: "))

    mensagens = []
    for i in range(pessoas):
        nome = input(f"\nDigite o nome da pessoa {i + 1}: ")
        mensagem = input(f"\nDigite a mensagem para a pessoa {i + 1}: ")
        hora = int(input(f"\nDigite a hora que deseja enviar a mensagem para a pessoa {i + 1}: "))
        minuto = int(input(f"\nDigite o minuto que deseja enviar a mensagem para a pessoa {i + 1}: "))
        mensagens.append((nome, mensagem, hora, minuto))

    print("\nTudo certo! Irei enviar suas mensagens!")

    foi_todos = False  # Boleano para o print ir só 1 vez
    counter = 0  # Counter to keep track of sent messages

    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min

        for mensagem in mensagens:
            enviado = enviar_mensagem(mensagem[0], mensagem, minute)
            if enviado:
                counter += 1

        if counter == len(mensagens) and not foi_todos:
            print("\n \033[1mENVIEI MSG PARA TODOS NA LISTA\033[😀")
            foi_todos = True

        if hour == 22 and not foi_todos:
            t = threading.Thread(target=selecUser)
            t.start()
            shopeeDiary()
            foi_todos = True

        time.sleep(31)

if __name__ == '__main__':
    run_at_specific_times()
