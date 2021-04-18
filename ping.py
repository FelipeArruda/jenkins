import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as numpy
from threading import Timer


def internet():
    df = []
    s = speedtest.SpeedTest()
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [data_atual, hora_atual, velocidade]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    Timer(1800, internet).start()

internet()