### 1

print("Hello World")

###  2

num = int(input("Digite um número: "))
print(f"O número que você digitou é {num}")

####  3

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(f"A soma dos dois números é {num1 + num2}")

####  4

notas = 0
for c in range(1, 5):
    notas += int(input(f"Digite a nota {c}: "))
print(notas/4)

###  5

metros = int(input("Digite um valor em metros para converter em centímetros"))
print(f"{metros}m é igual a {metros * 100}")

### 6

raio = int(input("Digite o valor do raio: "))
print(f"A área do círculo é {raio ** 2 * math.pi}")

### 7

