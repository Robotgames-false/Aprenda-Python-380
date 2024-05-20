
# Introdução ao Python: Elementos Básicos

# 🐍 Guia Básico do Python

Este código é uma introdução compacta aos elementos mais básicos do Python. Ele abrange diversos conceitos que são fundamentais para quem está começando a aprender a linguagem. Este pode ser um ótimo ponto de partida para explorar mais profundamente cada tópico.

## 📊 Variáveis

Demonstração de tipos básicos como inteiros, floats e strings.

## ➕ Operadores

Exemplo de operadores aritméticos e de comparação.

## 🔄 Estruturas de Controle

Demonstração de if-else, loop for e loop while.

## 🧮 Funções

Uma função simples que soma dois números.

## 📜 Listas e Foreach

Uso de uma lista e loop for para iterar sobre ela.

## 📚 Dicionários

Demonstração de um dicionário e iteração com `items()`.

## 🏛️ Classes e Objetos

Um exemplo simples de uma classe e como criar e usar um objeto.

## ⚠️ Exceções

Um bloco `try-except` para capturar uma exceção de divisão por zero.

```python
# 1. Variáveis
x = 10
y = 5.5
nome = "Python"

print("Variáveis:")
print(f"x = {x}, y = {y}, nome = {nome}\n")

# 2. Operadores
soma = x + y
produto = x * y
comparacao = x > y

print("Operadores:")
print(f"x + y = {soma}")
print(f"x * y = {produto}")
print(f"x > y? {comparacao}\n")

# 3. Estruturas de Controle (Condicionais e Loops)
idade = 18
print("Estruturas de Controle:")

# Condicional - if, elif, else
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Loop for
print("Loop for:")
for i in range(5):
    print(f"Iteração {i + 1}")

# Loop while
print("\nLoop while:")
contador = 0
while contador < 3:
    print(f"Contador é {contador}")
    contador += 1
print()

# 4. Funções
def soma_dois_numeros(a, b):
    return a + b

print("Funções:")
resultado = soma_dois_numeros(2, 3)
print(f"A soma de 2 e 3 é {resultado}\n")

# 5. Listas e Foreach
lista = ["Python", "JavaScript", "C++"]

print("Listas:")
for item in lista:
    print(f"Linguagem: {item}")

print()

# 6. Dicionários
dicionario = {
    "nome": "Python",
    "tipo": "Linguagem de Programação",
    "versao": 3.10
}

print("Dicionários:")
for chave, valor em dicionario.items():
    print(f"{chave}: {valor}")

print()

# 7. Classes e Objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa = Pessoa("Alice", 25)
print("Classes e Objetos:")
print(pessoa.saudacao())

print()

# 8. Exceções
print("Exceções:")
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

```

- Boolean
- ![.](https://github.com/elisioMassaqui/Aprenda-Python/blob/main/boolean%20in%20python.png)

- Comparação
- ![.](https://github.com/elisioMassaqui/Aprenda-Python/blob/main/compara%C3%A7%C3%A3o%20python.png)

- Matemática
- ![](https://github.com/elisioMassaqui/Aprenda-Python/blob/main/math%20in%20python.png)
