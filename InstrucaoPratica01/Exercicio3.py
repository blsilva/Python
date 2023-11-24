caractere_usuario = input("Digite um caractere: ")

if len(caractere_usuario) == 1:
    codigo_numerico = ord(caractere_usuario)
    codigo_octal = oct(codigo_numerico)
    codigo_hexadecimal = hex(codigo_numerico)
    
    print(f"'{caractere_usuario}' - Decimal: {codigo_numerico}, Octal: {codigo_octal}, Hexadecimal: {codigo_hexadecimal}")
else:
    print("Por favor, digite exatamente um caractere.")

#Em Python, os caracteres especiais, como 'ç' e 'ã',são tratados como parte da codificação de 
#caracteres utilizada.Python suporta Unicode, o que permite o uso de caracteres especiais e 
#a manipulação de diferentes conjuntos de caracteres.