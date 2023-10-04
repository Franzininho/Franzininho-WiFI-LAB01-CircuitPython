# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# Blinling LEDs
# Esse exemplo pisca os LEDs vermelho, verde e azul em sequência
# A cada segundo, um LED é ligado e desligado
# O LED vermelho está conectado ao pino IO14, o verde ao IO13 e o azul ao IO12

import board            # Biblioteca para acessar os recursos da placa
import digitalio        # Biblioteca para controlar os pinos digitais
import time             # Biblioteca para controlar o tempo

# Define os pinos para os LEDs vermelho, verde e azul
led_vermelho = digitalio.DigitalInOut(board.IO14)
led_verde = digitalio.DigitalInOut(board.IO13)
led_azul = digitalio.DigitalInOut(board.IO12)

# Configura os LEDs como saídas
led_vermelho.direction = digitalio.Direction.OUTPUT
led_verde.direction = digitalio.Direction.OUTPUT
led_azul.direction = digitalio.Direction.OUTPUT

# Lista dos LEDs
leds = [led_vermelho, led_verde, led_azul]

# Loop infinito para piscar os LEDs em sequência
while True:
    for led in leds:
        led.value = True  # Liga o LED
        time.sleep(1)     # Espera 1 segundo
        led.value = False # Desliga o LED
        time.sleep(1)     # Espera 1 segundo
