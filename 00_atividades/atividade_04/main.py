#biblioteca
import os
import time
import datetime

#declaração de variáveis
hora = datetime.datetime.now().strftime("%H:%M:%S")

#exibição o hora atual
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"hora atual: {hora}")
    time.sleep(1)
    