# Listas em Python

Uma ***list*** em python, nada mais é que uma coleção ordenada de valores, separados por vírgula e dentro de colchetes[]

Elas são usadas para armazenar diversos itens em uma única variável.
Ex:

```py
lista = ["Python Academy", "Academy"]
print(lista)
```

Podemos obersvar a classe de uma lista com type();

```py
lista = []
print(type(lista))
```

## Crinado listas de várias maneiras:

Lista com apenas um elemento:

```py
lista = ["PythonAcademy"]
print(lista)
```

Lista vazia:

```py
lista = []
print(lista)
```

Lista com diversos intes:

```py
lista = ["Python","Academy","2024"]
```

Também podemos usar a função list de próprio Python (built-in function):

```py
lista = list(["Python"])
```

Outra forma é criar listas resultantes de uma operação de "List Comprehensions".

```py
[item for item int iteravel]
```

Podemos criar listas através da função range()

```py
list(range(10))
```

Acessando dados da lista:
Todos os itens de uma lista são indexados, ou seja para cada item da lista um índice é atribuido da seguinte forma: lista[indice].

Exemplos com itens:

```py
frutas = ["Manga","Banana","Abacate","Laranja"]
```

E assim fica a sequência:
Indice: 0 | 2 | 3 | 4
Valores: Manga | Banana | Abacate | Laranja

Nesse caso:

```py
print(frutas[0])
```

saída: Manga

Agora sobre indexação negativa.
Que significa começar do fim, nesse caso.

Indice -5 | -4 | -3 | -2 | -1
Valores Manga | Banana | Jaca | Abacate | Abacaxi

```py
print(frutas[-1])
```

sáida: Abacaxi

Lista dentro de lista:
Suponha que exista uma lista dentro de uma lista, assim:

```py
lista = ["item",["Python", "Academy"], "item"]
```

Como podemos acessar o primeiro índice do item que é uma lista?
A resposta é simples, basta selecionar a posição em que se localiza a lista para ter acesso a ela, assim:

```py
sublista = lista[1]
print(sublista[0])
```

Ou ainda assim:

```py
print(lista[1][0])
```

Ambos obtemos o mesmo resultado!
"Python"

## Fatiando uma lista (slicing)

O fatiamento de listas, é a extração de um conjunto de elementos contidos numa lista:
***lista [inicio: fim: passo]***

Explicando cada elemento:
***início***: refere-se ao índice de ínicio do fatiamento.
***fim***: refere-se ao índice final do fatiamento. lista final não vai conter esse elemento.
***passo***: é um parâmentro opcional e é usado se pular elementos da lista.

Se quiser criar uma fatia de uma lista do índice 2 e 4, podemos fazer da seguinte forma:

```py
lista = [10, 20, 30, 40, 50, 60]
print(lista[2:5])
```

O slicing conta a partir do índice 2 até o índice 5 (mas não o usa), pegando os índices 2, 3, 4.
Saída: [30, 40, 50]

## Percorrendo listas

A forma mais comun é com loop foreach (for elemento in lista):

```py
lista = [20, 30 ,40]
for (num in lista):
print(num)
```

Saída: 10, 20, 30

Com a função enumerate() podemos percorrer também o índice referente a cada valor da lista:

```py
lista = [10, 20, 30, 40, 50, 60]
for indice, valor in enumerate(lista):
    print(f"indice = {indice}, valor = {valor}")
```

saida: indice = 0   valor = 10
              = 2         = 20
              = 3         = 30
              = 4         = 40
              = 5         = 50
              = 6         = 60
