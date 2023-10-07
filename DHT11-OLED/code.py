# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# DHT11, LDR e Display OLED
# Exemplo de leitura de temperatura e umidade com o sensor DHT11 e
# leitura de luminosidade com o LDR e exibição dos valores em um display OLED
# Necessário instalar a biblioteca adafruit_dht, adafruit_ssd1306 e adafruit_framebuf

import board
import busio
import adafruit_ssd1306
import time
import adafruit_dht
import analogio

# Define os pinos para o sensor DHT11 e LDR
pin_dht11 = board.IO15  # Substitua pelo pino correto
pin_ldr = board.IO1     # Substitua pelo pino correto

# Cria objetos para o sensor DHT11 e o LDR
dht11 = adafruit_dht.DHT11(pin_dht11)
ldr = analogio.AnalogIn(pin_ldr)

# Configuração do display OLED
i2c = busio.I2C(scl=board.IO9, sda=board.IO8)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Função para ler a luminosidade do LDR
def ler_luminosidade():
    return ldr.value

# Função para atualizar o display OLED com os valores de temperatura, umidade e luminosidade
def atualizar_display(temp, umid, luz):
    oled.fill(0)
    oled.text("Temp: {}C".format(temp), 0, 0, 1)
    oled.text("Umidade: {}%".format(umid), 0, 10, 1)
    oled.text("Luminosidade: {}".format(luz), 0, 20, 1)
    oled.show()

# Loop principal
while True:
    try:
        # Lê a temperatura e umidade do sensor DHT11
        temperatura = dht11.temperature
        umidade = dht11.humidity

        # Lê a luminosidade do LDR
        luminosidade = ler_luminosidade()

        # Atualiza o display OLED com os valores
        atualizar_display(temperatura, umidade, luminosidade)

    except RuntimeError as e:
        # Caso ocorra um erro na leitura do sensor, imprime uma mensagem de erro
        print("Erro na leitura:", e)

    # Aguarda um intervalo de tempo antes de realizar a próxima leitura e atualização do display
    time.sleep(1)  # Pode ajustar o intervalo conforme necessário
