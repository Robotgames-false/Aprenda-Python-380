n = "Imprimir apenas"
print("Hello Code Runnneeer\n")

n1 = "Soma basica"
x = 50
y = 79

resultado = x + y

print(f"Quando somamos {x} + {y} o resultado is = {resultado}\n")

n2 = "Definimos o metodo soma que retorna uma operation aritimetica e o resultado recebe o metodo com os seus paremetros."
def soma(a, b):
    return a + b

resultadoAB = soma(3, 47)
print("O retorno da soma(a, b) is:", resultadoAB,"\n")

n3 = "Aqui usamos alguns truques na string"
nome = "Elisio"
print("Oi:", f"({nome})", "Seja bem vindo ao Python com Coderunner\n")


n5 = "Numeros complexos"

r = 6
i = 4j

complexos = r + i
type(complexos) 

print("Numero imaginario: {}." .format(i))

bool(3 > 10)
print(bool)

n343 ="Imprime numero num alcance de 1 a 5 e reduz o outro pra negativo de -1 a -5 nesse caso o inverso "
numberRodada = 5

for rodada in range(1, 5):
    numberRodada -= 1 
    print(f"Number:{numberRodada}", rodada)

n4 = "Aqui recebe aoenas valores inteiros, faz a soma e imprime."
numero1 = int(input("Digite o primeiro numero:"))

numero2 = int(input("Digite o segundo numero:"))

resultadoNumero = numero1 + numero2

print("Ta aqui o resultado:", resultadoNumero)
