"""
Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao tentar executar
"""

print(123)
print(456)
#int('a')

# numero_str = input('digite um número para dobrar: ')
# numero_float = float(numero_str)
# if numero_str.isdigit():
#     print(numero_str.isdigit())
#     print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
# else:
#     print('Isso não é um número')

numero_str = input('digite um número para dobrar: ')
print(numero_str.isdigit())
try: #checa se possuí algum erro (except) enquanto executa o algoritmo
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except: #se tiver erro executa o algoritmo abaixo
    print('Isso não é um número')