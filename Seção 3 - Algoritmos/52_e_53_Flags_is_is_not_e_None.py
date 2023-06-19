""""
Flag (Bandeira) - Marcar um local
None == Não valor
is e is not == é ou não é (tipo, valor, identidade)
id == Identidade
"""

v1 = 'a'
print(id(v1)) # valor da variável na memória

condicao = False
passou_no_if = None # equivalente a false

if condicao:
    passou_no_if = True
    print('Faça')
if condicao:
    passou_no_if = False
    print('Não faça')

if passou_no_if is None:
    print('Não passou_no_if') # is testa a afirmativa para saber se é verdadeira
else:
    print('passou no if', passou_no_if is not None) # is testa a afirmativa para saber se é falsa