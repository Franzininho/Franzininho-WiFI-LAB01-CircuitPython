# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# Botões e LEDs
# Esse exemplo lê o estado de 3 botões e alterna o estado de 3 LEDs 
# quando os botões são pressionados. Um beep é emitido quando um botão
# é pressionado.O código utiliza o conceito de debounce para evitar 
# que o botão seja acionado mais de uma vez quando pressionado.
import board
import digitalio
import time

# Define os LEDs, botões e o buzzer
led_vermelho = digitalio.DigitalInOut(board.IO14)
led_verde = digitalio.DigitalInOut(board.IO13)
led_azul = digitalio.DigitalInOut(board.IO12)
botao1 = digitalio.DigitalInOut(board.IO7)
botao2 = digitalio.DigitalInOut(board.IO6)
botao3 = digitalio.DigitalInOut(board.IO5)
buzzer = digitalio.DigitalInOut(board.IO17)

led_vermelho.direction = digitalio.Direction.OUTPUT
led_verde.direction = digitalio.Direction.OUTPUT
led_azul.direction = digitalio.Direction.OUTPUT
botao1.direction = digitalio.Direction.INPUT
botao2.direction = digitalio.Direction.INPUT
botao3.direction = digitalio.Direction.INPUT
buzzer.direction = digitalio.Direction.OUTPUT

botao1.pull = digitalio.Pull.UP
botao2.pull = digitalio.Pull.UP
botao3.pull = digitalio.Pull.UP

# Inicialmente, desliga todos os LEDs, define os estados dos botões e desliga o buzzer
led_vermelho.value = False
led_verde.value = False
led_azul.value = False
buzzer.value = False

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

# Função para emitir um beep
def emitir_beep():
    buzzer.value = True
    time.sleep(0.1)  # Duração do beep (100 ms)
    buzzer.value = False

# Loop principal
while True:
    # Lê o estado atual dos botões
    estado_botao1_atual = not botao1.value
    estado_botao2_atual = not botao2.value
    estado_botao3_atual = not botao3.value
    
    # Verifica o Botão 1
    if estado_botao1_atual != ultimo_estado_botao1:
        tempo_ultimo_estado1 = time.monotonic()
        ultimo_estado_botao1 = estado_botao1_atual
    
    if (time.monotonic() - tempo_ultimo_estado1) >= debounce_interval:
        if estado_botao1_atual and botao1_state:
            led_vermelho.value = not led_vermelho.value
            emitir_beep()
            botao1_state = False
        
        if not estado_botao1_atual:
            botao1_state = True
    
    # Verifica o Botão 2
    if estado_botao2_atual != ultimo_estado_botao2:
        tempo_ultimo_estado2 = time.monotonic()
        ultimo_estado_botao2 = estado_botao2_atual
    
    if (time.monotonic() - tempo_ultimo_estado2) >= debounce_interval:
        if estado_botao2_atual and botao2_state:
            led_verde.value = not led_verde.value
            emitir_beep()
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
            emitir_beep()
            botao3_state = False
        
        if not estado_botao3_atual:
            botao3_state = True

