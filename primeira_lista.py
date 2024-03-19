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

aresta = int(iput('Digite o valor da aresta do quadrado: '))
print(f'O dobro da área do quadrado é {aresta ** 2 * 2}')

### 8

pHora = int(input('Digite quanto você ganha por hora: '))
horas = int(input('Digite quantas horas você trabalha por mês: '))

print(f'Você irá ganhar R${phora * horas:.2f} esse mês. ')

### 9 

f = int(input('Digite a temperatura em °F: '))
print(f'{f}°F são {(f - 32) / 1,8:.0f}')

### 10

c = int(input('Digite a temperatura em °C: '))
print(f'{c}°C são {c * 1.8 - 32}°F')

### 11

altura = int(input('Digite a sua altura e cm: '))
print(f'Seu peso ideal é de {(72*altura)-58}kg')

### 12

h = int(input('Digite a sua altura e cm: '))
print(f'Se você for homem o seu peso ideal é de {(72*h)-58}kg/nSe você for mulher seu peso ideal é de {(62.1*h)-44.7}')

### 13

exesso = 0
multa = 0

peso = int(input('Digite o peso em kg: '))

if peso > 50:
    exesso = peso - 50
    multa = exesso * 4

print(f'Houve um exesso de {exesso}kg e terá de pagar uma multa de R${multa:.2f}')

### 14

area = int(input('Digite a área em m² a ser pintada:'))

lata = 18*3
tot_latas = 0
preco = 80
tot_preco = 0

while lata * tot_lata < area:
    tot_lata += 1
    tot_preco += preco

print(f'Serão necessárias {tot_lata} latas de tintas, que sairão por R${tot_preco}')

### ATIV

import math

num = int(input('Digite um número que possue uma raíz quadrada inteira: '))

print(f'A raíz quadrada de {num} é {math.sqrt(num)}')