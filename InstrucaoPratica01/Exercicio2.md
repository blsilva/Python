# Demonstre como funcionam os operadores aritméticos e aritméticos compostos em Python e destaque as principais novidades e diferenças em relação ao conjunto de operadores com inteiros disponíveis em C/C++ ;

O tipo de dado que permite representar um subconjunto dos números inteiros em Python é conhecido como "int". Este tipo de dado é usado para representar números inteiros, positivos ou negativos, sem ponto decimal. Em Python, ao contrário de algumas outras linguagens como C/C++, os inteiros não têm limites fixos de tamanho, a menos que especificado por implementações específicas. Isso significa que você pode ter inteiros de qualquer tamanho em Python, sujeitos apenas aos limites da memória disponível.

Aqui estão alguns exemplos de como os operadores aritméticos e aritméticos compostos funcionam em Python, juntamente com algumas diferenças notáveis em relação a C/C++:

Operadores Aritméticos:

```python
# Adição
resultado = 5 + 3  # Resultado: 8

# Subtração
resultado = 7 - 4  # Resultado: 3

# Multiplicação
resultado = 6 * 2  # Resultado: 12

# Divisão (retorna um número de ponto flutuante)
resultado = 10 / 3  # Resultado: 3.333...

# Divisão inteira (descarta a parte fracionária)
resultado = 10 // 3  # Resultado: 3

# Módulo (resto da divisão)
resultado = 10 % 3  # Resultado: 1

# Exponenciação
resultado = 2 ** 3  # Resultado: 8
```

Operadores Aritméticos Compostos:
```python
# Adição
x = 5
x += 3  # x agora é 8

# Subtração
y = 7
y -= 4  # y agora é 3

# Multiplicação
z = 6
z *= 2  # z agora é 12

# Divisão
w = 10
w /= 3  # w agora é 3.333...
```
Principais Diferenças em Relação a C/C++:
1. Tamanho Dinâmico dos Inteiros: Em Python, os inteiros podem ter qualquer tamanho, enquanto em C/C++ o tamanho é geralmente fixo (por exemplo, int em C é geralmente 4 bytes).

2. Divisão Padrão: A divisão de dois inteiros em Python sempre retorna um número de ponto flutuante, mesmo se a divisão for exata.

3. Operador de Exponenciação: Em Python, o operador ** é usado para exponenciação, enquanto em C/C++ é necessário usar funções da biblioteca padrão ou bibliotecas específicas para calcular a potência.

4. Operadores Aritméticos Compostos: Python oferece operadores aritméticos compostos (por exemplo, +=, -=, *=, /=), o que pode levar a um código mais conciso e legível.

5. Ausência de Overflow ou Underflow: Diferentemente de algumas implementações em C/C++, Python lida automaticamente com overflow ou underflow em operações com inteiros, adaptando o tamanho necessário conforme a necessidade.

# Demonstre a possibilidade de representar números inteiros significativamente grandes calculando o fatorial de 30 e comparando o resultado com o maior valor inteiro que pode ser representado em C/C++;

Calculando o fatorial de 30 em Python e comparando o resultado com o maior valor inteiro que pode ser representado em C/C++. Em Python, os inteiros podem ter tamanho dinâmico e, portanto, não têm um limite fixo.

```python
# Calcular o fatorial de 30 em Python
fatorial_python = 1
for i in range(1, 31):
    fatorial_python *= i

# Imprimir o resultado
print(f'O fatorial de 30 em Python é: {fatorial_python}')

# Comparar com o maior valor inteiro em C/C++
# No caso comum de um int de 32 bits, o maior valor seria 2^31 - 1
maior_valor_int_c = 2**31 - 1

# Imprimir o maior valor inteiro em C/C++
print(f'O maior valor inteiro em C/C++ (32 bits) é: {maior_valor_int_c}')
```
Vale ressaltar que, em C/C++, o tipo de dado int de 32 bits tem um valor máximo de 2^31 - 1 (2147483647) se for sem sinal (unsigned) e 2^31 - 1 se for com sinal (signed). No entanto, em Python, o resultado do fatorial de 30 é significativamente maior do que o maior valor inteiro que pode ser representado em C/C++. Isso destaca a flexibilidade dos inteiros em Python, que podem crescer dinamicamente para acomodar valores maiores.

# As variáveis numéricas são imutáveis. Demonstre com exemplos asimplicações desta afirmação;

Sim, as variáveis numéricas em Python são imutáveis. Isso significa que, uma vez que você atribui um valor a uma variável numérica, não pode alterar diretamente esse valor. Qualquer operação que modifique o valor de uma variável numérica na verdade cria um novo valor e atribui à variável.

Eexemplos para ilustrar as implicações dessa imutabilidade:

Exemplo 1: Imutabilidade na Atribuição
```python
# Atribuição inicial
x = 5

# Tentativa de modificar o valor de x
x = x + 2  # Isso cria um novo valor (7) e o atribui a x

# Impressão do valor atual de x
print(x)  # Saída: 7
```
Exemplo 2: Imutabilidade nas Operações
```python
# Atribuição inicial
y = 10

# Tentativa de incrementar y diretamente
# Isso resultará em um erro
# y += 5  

# No entanto, você pode fazer uma operação e atribuir o resultado a y
y = y + 5  # Isso cria um novo valor (15) e o atribui a y

# Impressão do valor atual de y
print(y)  # Saída: 15
```
Exemplo 3: Função que Retorna um Novo Valor
```python
def multiplicar_por_dois(valor):
    return valor * 2

# Atribuição inicial
z = 3

# Chamar a função que retorna um novo valor e atribuir a z
z = multiplicar_por_dois(z)

# Impressão do valor atual de z
print(z)  # Saída: 6
```
Esses exemplos demonstram que, em cada caso, uma nova variável é criada e atribuída à variável original. Isso contrasta com tipos mutáveis, como listas, onde você pode modificar diretamente o conteúdo da lista sem criar uma nova lista. A imutabilidade em variáveis numéricas tem implicações em como você manipula esses valores em comparação com tipos mutáveis.

# Verifique quais métodos estão disponíveis para as variáveis inteiras;

Em Python, as variáveis inteiras (do tipo int) são objetos e têm métodos associados a elas. No entanto, como as variáveis inteiras são imutáveis, a maioria dos métodos associados a elas são métodos que retornam um novo objeto int com base em alguma operação, em vez de modificar o objeto original. Aqui estão alguns dos métodos disponíveis para variáveis inteiras em Python:

1. int.bit_length(): Retorna o número mínimo de bits necessários para representar o valor binário do número, excluindo o sinal e os zeros à esquerda.

```python
x = 42
print(x.bit_length())  # Saída: 6
```
2. int.to_bytes(length, byteorder, signed=False): Retorna uma representação de bytes do inteiro.

```python
x = 1234
bytes_representation = x.to_bytes(2, byteorder='big')
print(bytes_representation)  # Saída: b'\x04\xd2'
```
3. int.from_bytes(bytes, byteorder, signed=False): Converte uma representação de bytes de volta para um inteiro.

```python
bytes_representation = b'\x04\xd2'
x = int.from_bytes(bytes_representation, byteorder='big')
print(x)  # Saída: 1234
```
4. int.conjugate(): Retorna o conjugado do número complexo (o próprio número para inteiros).

```python
x = 5
print(x.conjugate())  # Saída: 5
```
5. int.real e int.imag: Partes real e imaginária do número complexo (0 para inteiros).

```python
x = 7
print(x.real)  # Saída: 7.0
print(x.imag)  # Saída: 0.0
```
6. int.__abs__(): Retorna o valor absoluto do inteiro.

```python
x = -10
abs_value = abs(x)
print(abs_value)  # Saída: 10
```