# Introdução ao SciDB

## Executando o container com o SciDB

Para inicializar o contêiner do SciDB, execute no terminal o seguinte comando:

```bash
docker run -it --name worcap-2017 esensing/scidb:16.9
```

Será aberta uma janela do terminal no contêiner. Torne-se usuário ```scidb```:
```
su - scidb
```
**Pronto !!!** Seu ambiente está pronto para executar as consultas que veremos ao longo do minicurso.

## Consultas

### Definindo um Array chamado ```mod13q1```

```bash
iquery -aq "CREATE ARRAY mod13q1 <nir:double, red:double, blue:double> [col_id=0:4,1,0, row_id=0:4,1,0, time_id=0:3,4,0];"
```

Para verificar se o array foi definido corretamente, utilize o seguinte comando:
```bash
iquery -aq "list('arrays');"
```

Esse array estará vazio, conforme pode ser visto com o comando abaixo:
```bash
iquery -aq "scan(mod13q1);"
```

### Criando um Array Temporário

Exemplo de geração de um atributo (sequencial):
```
iquery -aq "build(<nir:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5)/1.0));"
```

### Combinando dois arrays

```
iquery -aq "join(
              build(<nir:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5))/1.0),
              build(<nir:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5))/10.0)
            );"
```


### Gerando um array com três atributos
- nir = val/1.0
- red = val/10.0
- blue= val/100.0

```
iquery -aq "store(join(
                    join(
                        build(<val:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5))/1.0),
                        build(<val:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5))/10.0)
                        ), 
                    build(<val:double>[col_id=0:4,1,0,row_id=0:4,1,0,time_id=0:3,4,0],(col_id+(row_id*5)+time_id*(5*5))/100.0)
                  ), mod13q1);"
```


### Consultas
#### Slice horizontal
```
iquery -aq "subarray(mod13q1, 3, 1, 1, 3, 5, 4);"
```

#### Slice vertical
```
iquery -aq "subarray(mod13q1, 1, 3, 1, 5, 3, 4);"
```

#### Série temporal
```
iquery -aq "subarray(mod13q1, 3, 3, 1, 3, 3, 4);"
```

#### Subarray
```
iquery -aq "subarray(mod13q1, 2, 2, 1, 4, 4, 3)"
```
## NDVI
```
iquery -aq "store(project(apply(mod13q1,new_evi, 2.5*(nir-red)/(nir+6.0*red-7.5*blue+1.)), new_evi), evi_array);"
```


#### Quantis
```
iquery -aq "store(quantile(evi_array, 10, new_evi),mod13q1_evi_qntl);"
```

#### Janela 3x3
```
iquery -aq "store(window(evi_array, 0, 2, 0, 2, 0, 0, avg(new_evi)),mod13q1_evi_avg);"
```


## Stream

## Script para calcular média

Salve dentro do docker em ```/tmp/avg_time.py```:
```python
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
```
**Atenção**: Lembre-se de tornar o arquivo executável
```
chmod +x /tmp/avg_time.py
```

Execute o stream:
```
iquery -aq "stream(mod13q1, '/tmp/avg_time.py');"
```


