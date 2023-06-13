"""
Fatiamento de strings
0123456789
Olá_Mundo_
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá_Mundo_'
print(variavel[5])
print(variavel[-4])
print(variavel[4:9]) # fatiamento
print(variavel[4:]) # fatiamento
print(variavel[:5]) # fatiamento
print(len(variavel)) # conta caracteres
print(len(variavel[1:5])) # conta caracteres
print(variavel[0:len(variavel):1]) # imprime caracteres com passo
print(variavel[0:9:2]) # impreime caracteres com passo
print(variavel[len(variavel)::-1]) # inverte caracteres com passo e imprime
print(variavel[9::-1]) # inverte caracteres com passo e imprime
print(variavel[len(variavel)-1])