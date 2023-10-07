# SPDX-FileCopyrightText: 2023 Fabio Souza for Franzininho
#
# SPDX-License-Identifier: MIT
# DHT11
# Exemplo de leitura de temperatura e umidade com o sensor DHT11
# Necessário instalar a biblioteca adafruit_dht
import board
import adafruit_dht
import time

# Define o pino ao qual o sensor DHT11 está conectado
pin_dht11 = board.IO15  # Substitua pelo pino correto

# Cria um objeto DHT11
dht11 = adafruit_dht.DHT11(pin_dht11)

# Loop principal
while True:
    try:
        # Lê a temperatura e umidade do sensor DHT11
        temperatura = dht11.temperature
        umidade = dht11.humidity

        # Imprime os valores na porta serial
        print("Temperatura: {}°C".format(temperatura))
        print("Umidade: {}%".format(umidade))

    except RuntimeError as e:
        # Caso ocorra um erro na leitura do sensor, imprime uma mensagem de erro
        print("Erro na leitura do sensor DHT11:", e)

    # Aguarda um intervalo de tempo antes de realizar a próxima leitura
    time.sleep(2)  # Pode ajustar o intervalo de acordo com suas necessidades