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

Nesse caso: print(frutas[0])
saída: Manga
