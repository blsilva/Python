for i in range(10):
    caractere = chr(ord('0') + i)
    codigo_numerico = ord(caractere)
    codigo_octal = oct(codigo_numerico)
    codigo_hexadecimal = hex(codigo_numerico)
    
    print(f"'{caractere}' - Decimal: {codigo_numerico}, Octal: {codigo_octal}, Hexadecimal: {codigo_hexadecimal}")
