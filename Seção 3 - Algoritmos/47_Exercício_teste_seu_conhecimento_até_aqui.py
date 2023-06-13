"""
Exercício
"""
# Peça ao usuário para digitar seu nome
nome = input("Digite seu nome: ")
print()
# Peça ao usuário para digitar sua idade
idade = input("Digite sua idade: ")
print()
espaco = " "
# Se nome e idade forem digitados:
if nome and idade != None:
    # Exiba:
    # Seu nome é {nome}
    print(f'Seu nome é {nome}')
    # Seu nome invertido é {nome invertido}
    print(f'Seu nome invertido é{(nome[len(nome)::-1])}')
    # Seu nome contém (ou não) espaços
    if espaco in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    # Seu nome tem {n} letras
    print(f'Seu nome tem {len(nome)} letras')
    # A primeira letra do seu nome é {letra}
    print(f'A primeira letra do seu nome é {nome[0]}')
    # A última letra do seu nome é {letra}
    print(f'A última letra do seu nome é {(nome[len(nome)-1])}')
#Se nada for digitado em nome ou idade:
else:
    # exiba "Desculpe, você deixou campos vazios."
    print("Desculpe, você deixou campos vazios.")