"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1   # inicia em linha
while linha <= qtd_linhas:  # conta linha até qtd_linhas
    print(f'========== Linha {linha} ==========')
    coluna = 1  # reinicia as colunas
    while coluna <= qtd_colunas:    # conta coluna até a qtd_colunas
        print(f'linha = {linha}; coluna = {coluna};')
        coluna += 1 # adiciona +1 em coluna
    linha += 1  # adiciona +1 em linha

print('Acabou')