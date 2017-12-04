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

devtools::install_github("e-sensing/sits", ref = "9dc5e898e213260ee4b3e3271a7983f4463c138f")
library(sits)
```
