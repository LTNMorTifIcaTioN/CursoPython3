"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print('Digite um número inteiro: ')
try:
    numero = int(input())
    if type(numero) is int:
        inteiro = 'É número inteiro.'
        print(inteiro)
        modulo = numero % 2
        if modulo != 0:
            print('Número ímpar')
        else:
            print('Número par')
except:
    inteiro = 'Não é número inteiro.'
    print(inteiro)

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se o horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

try:
    hora = int(input('Digite uma Hora, ex 00: '))
    if hora >= 0 and hora <= 11:
        print('Bom Dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    else:
        print('Boa Noite')
except:
    print("Você não digitou uma hora")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva
'Seu nome é normal'; maior que 6 escreva 'Seu nome é muito grande'.
"""

nome = input('Digite seu Nome: ')
tamanho = (len(nome))

if tamanho <= 4:
    print('Seu nome é curto')
if tamanho == 5 or tamanho == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
