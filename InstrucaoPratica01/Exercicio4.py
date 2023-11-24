nome_completo = "Biancardy Lima"

partes_do_nome = nome_completo.split()
nome = partes_do_nome[0]
sobrenome = partes_do_nome[1] if len(partes_do_nome) > 1 else ""

if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabética.")
elif nome > sobrenome:
    print(f"{sobrenome} antecede {nome} na ordem alfabética.")
else:
    print("As duas variáveis são iguais na ordem alfabética.")

quantidade_caracteres_nome = len(nome)
quantidade_caracteres_sobrenome = len(sobrenome)
print(f"Quantidade de caracteres no nome: {quantidade_caracteres_nome}")
print(f"Quantidade de caracteres no sobrenome: {quantidade_caracteres_sobrenome}")

e_palindromo = nome == nome[::-1]
print(f"O nome '{nome}' é um palíndromo? {e_palindromo}")
