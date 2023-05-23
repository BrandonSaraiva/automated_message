# importações das bibliotecas e funções
import datetime

def hora_atual():
    # Pegando a hora atual
    agora = datetime.datetime.now()
    # Partindo o tempo
    horas = agora.hour
    minutos = agora.minute
    segundos = agora.second

    # Print formatado do horario atual
    horario_atual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    return horario_atual