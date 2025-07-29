"""

Em Python, o termo constante "não existe", ou seja, atua sempre como variável.
Para indicar que a variável deve atuar como uma constante, devemos escrevê-la em letra maiúscula.

"""

velocidade = 60
local_carro = 100

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # distancia onde o radar pega

velocidade_multado_radar_1 = velocidade > RADAR_1
range_maximo_multado = LOCAL_1 + RADAR_RANGE
range_minimo_multado = LOCAL_1 - RADAR_RANGE

try:
    if (
        range_maximo_multado >= local_carro >= range_minimo_multado
    ) and velocidade_multado_radar_1:
        print("Carrou multado no Radar 1.")
except:
    print("Não foi multado")
