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
