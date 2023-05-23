import datetime

def hora_atual():
    agora = datetime.datetime.now()
    horas = agora.hour
    minutos = agora.minute
    segundos = agora.second

    horario_atual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    return horario_atual