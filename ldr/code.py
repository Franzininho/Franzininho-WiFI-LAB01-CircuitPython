# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# LDR
# Esse código lê o valor do LDR e acende o LED vermelho quando a luminosidade
# está baixa e apaga o LED vermelho quando a luminosidade está alta.
# O LED vermelho está conectado ao pino IO14.
# O LDR está conectado ao pino IO1.
import board
import digitalio
import analogio
import time

# Define os pinos para o LDR e LEDs RGB
ldr_pin = board.IO1  # Pino para o LDR
led_vermelho = digitalio.DigitalInOut(board.IO14)
led_verde = digitalio.DigitalInOut(board.IO13)
led_azul = digitalio.DigitalInOut(board.IO12)
buzzer = digitalio.DigitalInOut(board.IO17)

# Configura os LEDs como saídas
led_vermelho.direction = digitalio.Direction.OUTPUT
led_verde.direction = digitalio.Direction.OUTPUT
led_azul.direction = digitalio.Direction.OUTPUT
buzzer.direction = digitalio.Direction.OUTPUT

led_vermelho.value = False
led_verde.value = False
led_azul.value = False
buzzer.value = False

# Configuração do LDR
ldr = analogio.AnalogIn(ldr_pin)

# Loop principal
while True:
    # Lê o valor do LDR e adiciona à lista de leituras antigas
    valor_ldr = ldr.value
        
    # Imprime o valor da luminosidade no monitor serial
    print("Valor do LDR:", ldr.value)
    
    if valor_ldr < 10000:
        led_vermelho.value = True
    elif valor_ldr > 20000:
        led_vermelho.value = False

