"""
CONSTANTE = "VARIÁVEIS" imutáveis, convencionou-se em letra maiúscula.
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""
velocidade = 61     # velocidade do carro
local_carro = 101   # localização do carro

RADAR_1 = 60        # velocidade máxima do radar 1
LOCAL_1 = 100       # localização do radar 1
RADAR_RANGE = 1     # alcance do radar

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                       local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and \
                         vel_carro_pass_radar_1 > RADAR_1
if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')