#1) ocupar vaga no estacionamento: lembrando que, o mesmo veículo não pode ocupar duas vagas. Sendo assim, se o veículo encontra-se estacionado, o sistema não permite a inclusão de um outro veículo com a mesma placa; A entrada no estacionamento ocorre pela registro da placa. A escolha da vaga será de modo aleatório dentre as vagas disponíveis livres. Para isto utilize a função random que simula a escolha da vaga pelo motorista. Outro ponto importante, verificar a disponbilidade de vaga, antes de liberar o estacionamento; 

#2) liberar vaga: nesta funcionalidade, certifique-se de que o veículo encontra-se estabcionado. O sistema permite a saída de veículos que tem registro de entrada;

#3) exibir as vagas disponíveis no estacionamento, informando por setor as vagas disponíveis;

#4) consultar veículo estacionado

#A estrutura de dados para o controle das vagas será o array da biblioteca numpy. Pode ser três array's, um para cada setor do estacionamento.

#Todo o sistema precisa ser codificado em blocos (funções), desta forma trará clareza no código.

#Esta atividade, além de aprofundar os conhecimentos em funções e array da biblioteca numpy,e da lógica da programação, ela simula alguns comportamentos que devemos adotar quando manipulamos tabelas do banco de dados: inclusão cujo registro é chave primária, consulta e exclusão de registro.  Importante, não vamos utilizar banco de dados para esta atividade. 

import array as arr
import numpy as np

carros = np.array([])
vagas = np.array([])