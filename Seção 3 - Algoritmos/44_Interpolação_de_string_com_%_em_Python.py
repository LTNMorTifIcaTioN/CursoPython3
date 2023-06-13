"""
Interpolação básica de strings
s - sring
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Nayan'
preco = 2123.15
variavel = '%s, o preço total foi R$%.2f ' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))