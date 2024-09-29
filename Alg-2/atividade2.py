import numpy as np
import random

setor_A = np.full(5, None)
setor_B = np.full(5, None)
setor_C = np.full(5, None)

veiculos_estacionados = []


def ocupar_vaga(placa):
    # Função para verificar se o carro já está estacionado em uma vaga
    if placa in veiculos_estacionados:
        print(f'O carro com a placa {placa} já está estacionado.')
        return

    # Verificar a disponibilidade das vagas
    for setor in [setor_A, setor_B, setor_C]:
        vagas_disponiveis = [i for i, vaga in enumerate(setor) if vaga is None]
        if vagas_disponiveis:
            indice_vaga = random.choice(vagas_disponiveis)
            setor[indice_vaga] = placa
            veiculos_estacionados.append(placa)
            print(f'O carro com a placa {placa} foi estacionado na vaga {indice_vaga + 1}.')
            return
    print('Não há vagas disponíveis.')

def liberar_vaga(placa):
    for setor in [setor_A, setor_B, setor_C]:
        if placa in setor:
            indice_vaga = np.where(setor == placa)[0][0]
            setor[indice_vaga] = None
            veiculos_estacionados.remove(placa)
            print(f'O carro com a placa {placa} foi liberado da vaga {indice_vaga + 1}.')
            return
    print('Veículo não encontrado.')

def exibir_vagas_disponiveis():
    for i, setor in enumerate([setor_A, setor_B, setor_C], start=1):
        vagas_disponiveis = [j + 1 for j, vaga in enumerate(setor) if vaga is None]
        print(f'Setor {chr(64 + i)}: Vagas disponíveis - {vagas_disponiveis}')

def consultar_veiculo(placa):
    for i, setor in enumerate([setor_A, setor_B, setor_C], start=1):
        if placa in setor:
            indice_vaga = np.where(setor == placa)[0][0]
            print(f'O veículo com a placa {placa} está no setor {chr(64 + i)}, vaga {indice_vaga + 1}.')
            return
    print('Veículo não encontrado.')
