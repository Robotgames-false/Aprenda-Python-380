//Imprimir apenas
print("Hello Code Runnneeer\n")

//Soma basica
x = 50
y = 79

resultado = x + y

print(f"Quando somamos {x} + {y} o resultado is = {resultado}\n")

//Definimos o metodo soma que retorna uma operation aritimetica e o resultado recebe o metodo com os seus paremetros.
def soma(a, b):
    return a + b

resultadoAB = soma(3, 47)
print("O retorno da soma(a, b) is:", resultadoAB,"\n")

//Aqui usamos alguns truques na string
nome = "Elisio"
print("Oi:", f"({nome})", "Seja bem vindo ao Python com Coderunner\n")

//Aqui recebe aoenas valores inteiros, faz a soma e imprime.
numero1 = int(input("Digite o primeiro numero:"))

numero2 = int(input("Digite o segundo numero:"))

resultadoNumero = numero1 + numero2

print("Ta aqui o resultado:", resultadoNumero)
