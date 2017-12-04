# Installing SITS on Ubuntu 16.04

In the terminal type the following commands in order to install required 3rd-party libraries:

```bash
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
```

```bash
sudo apt-get update
```

```bash
sudo apt-get install libcurl4-openssl-dev libssl-dev openssl \
     git libxml2-dev libproj-dev libudunits2-dev libgdal20 \
     gdal-bin libgdal-dev
```

In the R environment:

```R
install.packages("devtools")

devtools::install_github("e-sensing/sits")
library(sits)
```




sudo apt-get install libcurl4-openssl-dev libssl-dev openssl git libxml2-dev libproj-dev libgdal-dev libudunits2-dev


R


install.packages("devtools", repos="https://ftp.gwdg.de/pub/misc/cran")
library(devtools)


install.packages("tidyverse")
library(tidyverse)


install.packages("parallel")   => Na versão 3.4.1 esse pacote já é basico do R e não precisa ser instalado
library(parallel)


install.packages("plyr")       => já é instalado junto com o tidyverse
library(plyr)

install.packages("rgdal")
library(rgdal)

install.packages("sf")
library(sf)

install.packages("rgl")

install.packages("TSdist")

#install.packages("dtwSat")
#library(dtwSat)

#devtools::install_github("e-sensing/sits", ref = "8fe5a04")
devtools::install_github("e-sensing/sits")
library(sits)


Se for necessário remover o SITS:
    detach(2, unload = TRUE)
    remove.packages("sits")
    library(sits)
    devtools::install_github("e-sensing/sits", ref = "8fe5a04")



 
Exemplos:

install.packages(c("nycflights13", "gapminder", "Lahman"))







sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libcurl4-openssl-dev libssl-dev openssl git libxml2-dev libproj-dev libudunits2-dev libgdal20 gdal-bin libgdal-dev libgl1-mesa-dev freeglut3 freeglut3-dev
install.packages("devtools", repos="https://ftp.gwdg.de/pub/misc/cran")
library(devtools)
devtools::install_github("e-sensing/sits")
library(sits)
#sudo apt-get remove libgdal-dev

