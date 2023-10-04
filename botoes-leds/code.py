# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# Botões e LEDs
# Esse exemplo lê o estado de 3 botões e alterna o estado de 3 LEDs 
# quando os botões são pressionados.
# O código utiliza o conceito de debounce para evitar 
# que o botão seja acionado mais de uma vez quando pressionado.

import board
import digitalio
import time

# Define os LEDs e botões
led_vermelho = digitalio.DigitalInOut(board.IO14)
led_verde = digitalio.DigitalInOut(board.IO13)
led_azul = digitalio.DigitalInOut(board.IO12)
botao1 = digitalio.DigitalInOut(board.IO7)
botao2 = digitalio.DigitalInOut(board.IO6)
botao3 = digitalio.DigitalInOut(board.IO5)

led_vermelho.direction = digitalio.Direction.OUTPUT
led_verde.direction = digitalio.Direction.OUTPUT
led_azul.direction = digitalio.Direction.OUTPUT
botao1.direction = digitalio.Direction.INPUT
botao2.direction = digitalio.Direction.INPUT
botao3.direction = digitalio.Direction.INPUT

botao1.pull = digitalio.Pull.UP
botao2.pull = digitalio.Pull.UP
botao3.pull = digitalio.Pull.UP

# Inicialmente, desliga todos os LEDs e define os estados dos botões
led_vermelho.value = False
led_verde.value = False
led_azul.value = False

botao1_state = True
botao2_state = True
botao3_state = True

# Variáveis para debounce
ultimo_estado_botao1 = True
ultimo_estado_botao2 = True
ultimo_estado_botao3 = True
tempo_ultimo_estado1 = 0
tempo_ultimo_estado2 = 0
tempo_ultimo_estado3 = 0
debounce_interval = 0.05  # Tempo de debounce em segundos

# Loop principal
while True:
    # Lê o estado atual dos botões
    estado_botao1_atual = not botao1.value
    estado_botao2_atual = not botao2.value
    estado_botao3_atual = not botao3.value
    
    # Verifica o Botão 1
    if estado_botao1_atual != ultimo_estado_botao1: # Se o estado mudou
        tempo_ultimo_estado1 = time.monotonic()     # Salva o tempo
        ultimo_estado_botao1 = estado_botao1_atual  # Salva o estado
    
    if (time.monotonic() - tempo_ultimo_estado1) >= debounce_interval:  # Se passou o tempo de debounce
        if estado_botao1_atual and botao1_state:                        # Se o botão está pressionado e o estado é True
            led_vermelho.value = not led_vermelho.value                 # Alterna o estado do LED
            botao1_state = False                                        # Salva o estado do botão
        
        if not estado_botao1_atual:                                     # Se o botão não está pressionado
            botao1_state = True                                         # Salva o estado do botão
    
    # Verifica o Botão 2
    if estado_botao2_atual != ultimo_estado_botao2:
        tempo_ultimo_estado2 = time.monotonic()
        ultimo_estado_botao2 = estado_botao2_atual
    
    if (time.monotonic() - tempo_ultimo_estado2) >= debounce_interval:
        if estado_botao2_atual and botao2_state:
            led_verde.value = not led_verde.value
            botao2_state = False
        
        if not estado_botao2_atual:
            botao2_state = True
    
    # Verifica o Botão 3
    if estado_botao3_atual != ultimo_estado_botao3:
        tempo_ultimo_estado3 = time.monotonic()
        ultimo_estado_botao3 = estado_botao3_atual
    
    if (time.monotonic() - tempo_ultimo_estado3) >= debounce_interval:
        if estado_botao3_atual and botao3_state:
            led_azul.value = not led_azul.value
            botao3_state = False
        
        if not estado_botao3_atual:
            botao3_state = True

