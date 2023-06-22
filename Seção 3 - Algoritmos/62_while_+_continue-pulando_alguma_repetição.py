"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f'Não vou mostrar o {contador}')
        continue    # quebra o laço e volta ao ponto de partida

    if contador >= 6 and contador <= 27:
        print(f'Não vou mostrar o {contador}')
        continue    # quebra o laço e volta ao ponto de partida

    print(contador)

    if contador == 40:
        break   # quebra o laço e finaliza.