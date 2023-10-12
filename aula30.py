"""
CONSTANTE =  Variaveis que não v]ao mudar.
Muitas condições no mesmo if (ruim)
        <-Contagem de complexidade (ruim)
"""

velocidade = 61 # Velocidade atual do carro 
local_docarro = 90 # Local onde o carro esta na estrada

RADAR_1 = 60 # Velocidade Maxima do Radar 1
LOCAL_1 = 100 # Local onde o radar 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
Carro_passou_do_radar1 = local_docarro >= (LOCAL_1 - RADAR_RANGE) and \
   local_docarro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 =  Carro_passou_do_radar1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if Carro_passou_do_radar1:
    print('Carro passou radar 1')

if carro_multado_radar1:
    print('Carro multado em radar 1')