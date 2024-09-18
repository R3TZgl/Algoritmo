import array as arr
import numpy as np


#10
notas = np.array([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 7.5, 8.0, 9.5, 7.0, 8.0, 6.5, 7.5, 8.0])

media = np.mean(notas)
print(f"A média geral é: {media}")


#11
vetor = np.array([1.5, -2.3, 3.1, -4.6, 5.0, -6.7, 7.8, -8.9, 9.2, -10.1])

negativos = np.sum(vetor < 0)
soma_positivos = np.sum(vetor[vetor > 0])

print(f"Quantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")


#12
num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print("Vetor original:", num)

for i in range(10):
    num[i], num[19 - i] = num[19 - i], num[i]

print("Vetor modificado:", num)


#13
num_candidatos = int(input("Informe o número de candidatos: "))
num_votantes = int(input("Informe o número de votantes: "))

votos = np.zeros(num_candidatos, dtype=int)

for i in range(num_votantes):
    voto = int(input(f"Votante {i+1}, informe o número do candidato (1 a {num_candidatos}): "))
    if 1 <= voto <= num_candidatos:
        votos[voto - 1] += 1
    else:
        print("Voto inválido!")

for i in range(num_candidatos):
    print(f"Candidato {i+1} recebeu {votos[i]} votos.")

#14
def ler_matriculas():
    matriculas = []
    while len(matriculas) < 100:
        matricula = int(input(f"Informe a matrícula do aluno {len(matriculas) + 1}: "))
        if matricula not in matriculas:
            matriculas.append(matricula)
        else:
            print("Matrícula já existente. Informe outra matrícula.")
    return matriculas

matriculas = ler_matriculas()

print("Matrículas dos alunos:", matriculas)


#15
def ler_vetor(tamanho):
    vetor = []
    for _ in range(tamanho):
        while True:
            try:
                elemento = int(input("Digite um número inteiro: "))
                vetor.append(elemento)
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return np.array(vetor)

def separar_pares_impares(vetor):
    pares = vetor[vetor % 2 == 0]
    impares = vetor[vetor % 2 != 0]
    return pares, impares

N = int(input("Digite o tamanho do vetor: "))
vetor_original = ler_vetor(N)

pares, impares = separar_pares_impares(vetor_original)

print("Vetor original:", vetor_original)
print("Vetor de pares:", pares)
print("Vetor de ímpares:", impares)


#16 A
def ler_vetor_ordenado(tamanho):
    vetor = []
    for _ in range(tamanho):
        while True:
            try:
                elemento = int(input("Digite um número inteiro: "))
                vetor.append(elemento)
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return np.array(sorted(vetor))

N = int(input("Digite o tamanho do vetor A: "))
M = int(input("Digite o tamanho do vetor B: "))

vetorA = ler_vetor_ordenado(N)
vetorB = ler_vetor_ordenado(M)

print("Vetor A:", vetorA)
print("Vetor B:", vetorB)

#B
def intercalar_vetores(vetorA, vetorB):
    vetorC = np.empty(len(vetorA) + len(vetorB), dtype=int)
    i = j = k = 0

    while i < len(vetorA) and j < len(vetorB):
        if vetorA[i] < vetorB[j]:
            vetorC[k] = vetorA[i]
            i += 1
        else:
            vetorC[k] = vetorB[j]
            j += 1
        k += 1

    while i < len(vetorA):
        vetor_C[k] = vetorA[i]
        i += 1
        k += 1

    while j < len(vetorB):
        vetor_C[k] = vetorB[j]
        j += 1
        k += 1

    return vetorC

vetorC = intercalar_vetores(vetorA, vetorB)
print("Vetor C:", vetorC)

#C
def ler_vetor_ordenado(tamanho):
    vetor = []
    for _ in range(tamanho):
        while True:
            try:
                elemento = int(input("Digite um número inteiro: "))
                vetor.append(elemento)
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
    return np.array(sorted(vetor))

def intercalar_vetores(vetorA, vetorB):
    vetorC = np.empty(len(vetor_A) + len(vetor_B), dtype=int)
    i = j = k = 0

    while i < len(vetor_A) and j < len(vetor_B):
        if vetor_A[i] < vetor_B[j]:
            vetor_C[k] = vetor_A[i]
            i += 1
        else:
            vetor_C[k] = vetor_B[j]
            j += 1
        k += 1

    while i < len(vetor_A):
        vetor_C[k] = vetor_A[i]
        i += 1
        k += 1

    while j < len(vetor_B):
        vetor_C[k] = vetor_B[j]
        j += 1
        k += 1

    return vetor_C

N = int(input("Digite o tamanho do vetor A: "))
M = int(input("Digite o tamanho do vetor B: "))

vetor_A = ler_vetor_ordenado(N)
vetor_B = ler_vetor_ordenado(M)

vetor_C = intercalar_vetores(vetor_A, vetor_B)
print("Vetor C:", vetor_C)


#17
notas = np.array([9.9, 9.7, 9.8, 10, 10])

notas = np.delete(notas, np.argmax(notas))
notas = np.delete(notas, np.argmin(notas)) 

media_final = np.mean(notas)

print(f'A média final do quesito é: {media_final:.2f}')