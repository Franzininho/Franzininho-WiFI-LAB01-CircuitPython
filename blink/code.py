# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# Blinling LED
# Esse exemplo pisca o LED verde a cada segundo
# O LED verde está conectado ao pino IO13 da placa Franzininho WIFI

import board            # Biblioteca para acessar os recursos da placa
import digitalio        # Biblioteca para controlar os pinos digitais
import time             # Biblioteca para controlar o tempo

# Define o pino do LED verde
led_verde = digitalio.DigitalInOut(board.IO13)
led_verde.direction = digitalio.Direction.OUTPUT

# Loop infinito para piscar o LED vermelho
while True:
    led_verde.value = not led_verde.value  # Inverte o estado do LED
    time.sleep(1)  # Espera 1 segundo
