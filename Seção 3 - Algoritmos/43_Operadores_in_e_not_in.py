# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4
# N A Y A N
# -5-4-3-2-1
"""nome = 'Nayan'
print(nome[2])
print(nome[-4])
print(20 * '-')
print('y' in nome)
print('e' in nome)
print(20 * '-')
print('yan' in nome)
print('vio' in nome)
print(20 * '-')
print('yan' not in nome)
print('vio' not in nome)"""

nome = input('Digite um Nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')