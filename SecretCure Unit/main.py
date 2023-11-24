from machine import Pin, I2C
import ssd1306
import urequests
import time
import random

# Configuração do display OLED
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 32  # Ajuste na altura para uma tela menor
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Dicas de saúde mental e informações sobre febre
dicas_saude_mental = [
    "Respire.",
    "caminhada.",
    "musica.",
    "Converse.",
]

info_febre = [
    "Descanse.",
    "banho morno.",
    "Compressa.",
    "Bebe agua."
]

# Função para mostrar mensagem na tela
def mostrar_mensagem_na_tela(mensagem):
    oled.fill(0)
    lines = [mensagem[i:i + 21] for i in range(0, len(mensagem), 21)]  # Quebra a mensagem em linhas
    for i, line in enumerate(lines):
        oled.text(line, 0, i * 10)
    oled.show()
    time.sleep(3)

# Função para mostrar dicas de saúde mental
def mostrar_dicas_saude_mental():
    dica = random.choice(dicas_saude_mental)
    mostrar_mensagem_na_tela(dica)

# Função para mostrar informações sobre febre
def mostrar_info_febre():
    info = random.choice(info_febre)
    mostrar_mensagem_na_tela(info)

# Loop principal
while True:
    oled.fill(0)
    oled.text('Qual sintoma:', 0, 5)
    oled.text('1. Saude Mental', 0, 20)
    oled.text('2. Febre', 0, 35)
    oled.show()

    escolha = input("Digite 1 ou 2: ")

    try:
        escolha = int(escolha)
        if escolha == 1:
            mostrar_dicas_saude_mental()
        elif escolha == 2:
            mostrar_info_febre()

        # Simulação de recomendação de solução
        oled.fill(0)
        if escolha == 1:
            oled.text('Solucao:', 0, 5)
            oled.text('Descanse', 0, 20)
        elif escolha == 2:
            oled.text('Solucao:', 0, 5)
            oled.text('Beba agua', 0, 20)
        oled.show()
        time.sleep(3)
        
        # Volta à tela inicial após um tempo
        oled.fill(0)
        oled.show()
        time.sleep(3)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
