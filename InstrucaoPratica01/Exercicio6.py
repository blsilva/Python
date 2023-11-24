L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(L[::-1])   # Reverte a lista
print(L[-1::])    # Último elemento da lista
print(L[:-1:])    # Todos os elementos, exceto o último
print(L[::-2])    # Reverte e pega elementos alternados
print(L[-2::])    # Do penúltimo até o final
print(L[:-2:])    # Todos os elementos, exceto os dois últimos

# Determinação do signo do zodíaco chinês
ano_nascimento = int(input("Digite o ano de nascimento: "))
signos_chineses = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

signo = signos_chineses[ano_nascimento % 12]

print(f"\nO signo do zodíaco chinês para o ano de {ano_nascimento} é: {signo}")
