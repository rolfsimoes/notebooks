#!/usr/bin/python

import sys
end_of_interaction = 0

while (end_of_interaction != 1):
  header = sys.stdin.readline().rstrip()
  if(header != "0"):
    # Numero de linhas recebidas
    num_lines = int(header)
    
    # arrays dos atributos
    nir = []
    red = []
    blue = []

    # para cada linha (tempo)
    for i in range(0, num_lines):
      # le a linha "nir		red	blue"
      line = sys.stdin.readline().rstrip()

      # converte a linha para um array de inteiros
      line = [float(t) for t in line.split('\t')]

      # adiciona cada atributo no seu respectivo array
      nir.append(line[0])
      red.append(line[1])
      blue.append(line[2])
   
    # Calculando medias
    avg_nir = sum(nir)/len(nir)
    avg_red = sum(red)/len(red)
    avg_blue = sum(blue)/len(blue)

    # Saida
    print(1)
    print(avg_nir, avg_red, avg_blue)    

    # garante que os dados serao enviados para stdout
    sys.stdout.flush()

  else:

    # Se recebeu "0", entao nao ha mais dados para receber    
    end_of_interaction = 1
    print("0")

    # garante que os dados serao enviados para stdout
    sys.stdout.flush()
