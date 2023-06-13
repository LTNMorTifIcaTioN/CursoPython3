"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r '__repr__' !s '__str__' !a '__asc__'
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preenche com caractere o lado esquerdo
print(f'{variavel: <10}.') # preenche com caractere o lado direito
print(f'{variavel:$^10}.') # alinha no centro com preenchimento pela esquerda e direita
print(f'{1000.14565485212354856213:.1f}')
print(f'{1000.14565485212354856213:,.1f}')
print(f'{1000.14565485212354856213:+10,.1f}')
print(f'{1000.14565485212354856213:0=+10,.1f}')
print(f'O Hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')