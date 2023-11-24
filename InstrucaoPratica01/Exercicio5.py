import sys

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

maior_potencia_de_2 = sys.float_info.max_exp
menor_potencia_de_2 = sys.float_info.min_exp

print(f"\nMaior potência de 2 representável com float: 2^{maior_potencia_de_2}")
print(f"Menor potência de 2 representável com float: 2^{menor_potencia_de_2}")
