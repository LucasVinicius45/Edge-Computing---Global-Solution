from machine import Pin, I2C
import ssd1306

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Função para mostrar a descrição do sintoma
def mostrar_descricao_sintoma(opcao):
    oled.fill(0)  # Limpa a tela
    if opcao == 1:
        descricao = "Caminhe"
    elif opcao == 2:
        descricao = "Descanse"
    else:
        descricao = "Opção inválida."

    # Mostra a descrição do sintoma
    oled.text(descricao, 20, 20)
    oled.show()

while True:
    # Mensagem principal e opções de sintomas
    oled.text('Escolha:', 10, 15)
    oled.text('1. Saude Mental', 10, 30)
    oled.text('2. Febre', 10, 50)
    oled.show()

    # Aguarda a entrada do usuário
    escolha = input("Digite 1 ou 2: ")

    try:
        escolha = int(escolha)
        if escolha in [1, 2]:
            mostrar_descricao_sintoma(escolha)
            break  # Sai do loop após a escolha válida
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
