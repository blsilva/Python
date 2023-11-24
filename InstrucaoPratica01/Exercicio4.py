nome_completo = "Biancardy Lima"

posicao_ultimo_espaco = nome_completo.rfind(" ")

if posicao_ultimo_espaco != -1:
    nome = nome_completo[:posicao_ultimo_espaco]
    sobrenome = nome_completo[posicao_ultimo_espaco + 1:]
else:
    nome = nome_completo
    sobrenome = ""

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
