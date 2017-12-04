# SciDB introduction

## Running SciDB container

To start the SciDB container, execute in the terminal the following command:

```bash
docker run -it --name geoinfo-2017 esensing/scidb:16.9
```

In the opened terminal, type the following command in order to change to user ```scidb```:

```
su - scidb
```
**Done !!!** Your environment ir ready to perform the queries that we will use on this short-course.

## Queries

### Defining Array: ```mod13q1```

```bash
iquery -aq "CREATE ARRAY mod13q1 <nir:double, red:double, blue:double> [col_id=0:4,1,0, row_id=0:4,1,0, time_id=0:3,4,0];"
```

In order to check if the array created in the last step was correctly defined, type the following command in the terminal:

```bash
iquery -aq "list('arrays');"
```

We can verify that this array is empty using the following command:
```bash
iquery -aq "scan(mod13q1);"
```

### Creating an array with 3 attributes (nir, red, blue): ```mod13q1```

Type the following command in the terminal in order to create an array with 3 attributes (nir, red, blue) with values in sequential order. 
Different scales was used in each attribute:
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


### Queries

#### Horizontal Slice
```
iquery -aq "subarray(mod13q1, 0, 2, 0, 4, 2, 3);"
```

#### Time Series
```
iquery -aq "subarray(mod13q1, 2, 2, 0, 2, 2, 3);"
```

## NDVI
```
iquery -aq "store(project(apply(mod13q1,new_evi, 2.5*(nir-red)/(nir+6.0*red-7.5*blue+1.)), new_evi), evi_array);"
```

#### Window Queries
```
iquery -aq "store(window(evi_array, 0, 2, 0, 2, 0, 0, avg(new_evi)),mod13q1_evi_avg);"
```

## SciDB Stream

## Calculating the average of time series

In order to download the example script, type the following command in the container terminal:

```
wget https://raw.githubusercontent.com/e-sensing/notebooks/master/worcap-2017/scidb/avg_time.py -O /tmp/avg_time.py
```

O conteúdo do script ```avg_time.py``` segue abaixo:
```python
#!/usr/bin/python

import sys
end_of_interaction = 0

while (end_of_interaction != 1):
  header = sys.stdin.readline().rstrip()
  if(header != "0"):
    # received lines
    num_lines = int(header)
    
    # attributes
    nir = []
    red = []
    blue = []

    # for each timestamp
    for i in range(0, num_lines):
      # read the line "nir		red	  blue"
      line = sys.stdin.readline().rstrip()

      # extract each attribute from string and converts to float
      line = [float(t) for t in line.split('\t')]

      # add each attribute to the respective array
      nir.append(line[0])
      red.append(line[1])
      blue.append(line[2])
   
    # Calculating the averages
    avg_nir = sum(nir)/len(nir)
    avg_red = sum(red)/len(red)
    avg_blue = sum(blue)/len(blue)

    # Output
    print(1)
    print(avg_nir, avg_red, avg_blue)

    sys.stdout.flush()

  else:

    # If "0", no more data will be received
    end_of_interaction = 1
    print("0")

    sys.stdout.flush()
```
**Attention**: Modify the file permission
```
chmod +x /tmp/avg_time.py
```

Type the following command in the terminal in order to execute the stream:
```
iquery -aq "stream(mod13q1, '/tmp/avg_time.py');"
```

