# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# Botão e LED com debounce
# Esse exemplo lê o estado de um botão e inverte o LED quando o botão é pressionado.
# O código possui um mecanismo de debounce para evitar que o LED inverta várias vezes

import board
import digitalio
import time

# Define os pinos para os LEDs e o botão
led_vermelho = digitalio.DigitalInOut(board.IO14)
led_verde = digitalio.DigitalInOut(board.IO13)
led_azul = digitalio.DigitalInOut(board.IO12)
botao1 = digitalio.DigitalInOut(board.IO7)

# Configura os LEDs como saídas
led_vermelho.direction = digitalio.Direction.OUTPUT
led_verde.direction = digitalio.Direction.OUTPUT
led_azul.direction = digitalio.Direction.OUTPUT

# Configura o botão como entrada com pull-up
botao1.direction = digitalio.Direction.INPUT
botao1.pull = digitalio.Pull.UP

# Inicialmente, desliga todos os LEDs
led_vermelho.value = False
led_verde.value = False
led_azul.value = False

estado_led_vermelho = False

# Variáveis para debounce
ultimo_estado_botao = True
tempo_ultimo_estado = 0
debounce_interval = 0.05  # Tempo de debounce em segundos

# Loop principal
while True:
    # Lê o estado atual do botão
    estado_botao_atual = not botao1.value  # Inverte o valor lido pois o botão está em pull-up
    
    # Verifica se o estado do botão mudou
    if estado_botao_atual != ultimo_estado_botao:
        tempo_ultimo_estado = time.monotonic()  # Registra o momento da mudança
        ultimo_estado_botao = estado_botao_atual
    
    # Verifica se o botão está estável após o tempo de debounce
    if (time.monotonic() - tempo_ultimo_estado) >= debounce_interval:
        if estado_botao_atual and botao1_state:
            # Inverte o estado do LED vermelho
            led_vermelho.value = not led_vermelho.value
            botao1_state = False  # Define o estado do botão como falso
        
        if not estado_botao_atual:
            botao1_state = True  # Define o estado do botão como verdadeiro
