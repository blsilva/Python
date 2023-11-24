a = 5.0
b = 2.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
exponenciacao = a ** b

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {exponenciacao}")

x = 10.0
y = 3.0

x += y 
print(f"x depois de adição: {x}")

x -= y  
print(f"x depois de subtração: {x}")

x *= y  
print(f"x depois de multiplicação: {x}")

x /= y  
print(f"x depois de divisão: {x}")

x **= y  
print(f"x depois de exponenciação: {x}")

# Maior e menor potência de 2 representável com float
import sys

maior_potencia_de_2 = sys.float_info.max_exp
menor_potencia_de_2 = sys.float_info.min_exp

print(f"\nMaior potência de 2 representável com float: 2^{maior_potencia_de_2}")
print(f"Menor potência de 2 representável com float: 2^{menor_potencia_de_2}")

# Demonstração da imutabilidade de variáveis numéricas
num_inteiro = 5

# Criando uma nova variável com o resultado da operação
novo_num_inteiro = num_inteiro + 2

print(f"\nValor original: {num_inteiro}")
print(f"Novo valor após operação: {novo_num_inteiro}")

# Verificação dos métodos disponíveis para variáveis de ponto flutuante
num_ponto_flutuante = 3.14

# Mostrando os métodos disponíveis para variáveis de ponto flutuante
print("\nMétodos disponíveis para variáveis de ponto flutuante:")
print(dir(num_ponto_flutuante))
