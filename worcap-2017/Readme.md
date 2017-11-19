# Preparação do Ambiente Computacional para o Minicurso **Geospatial Big Data**

## Instalação do Docker

Instale o [Docker](https://www.docker.com) em seu computador.

Se você utiliza a distribuição Linux Ubuntu 16.04, você pode seguir o passo-a-passo [aqui](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-16-04-pt), caso contrário siga as instruções do [site do Docker](https://www.docker.com/community-edition).

Após a instalação do Docke, siga as instruções abaixo para instalar as imagens dos containers que serão utilizadas no minicurso.


## Baixando imagem esensing/scidb:16.9

Para baixar a imagem do container scidb para a realização das atividades práticas do minicurso, execute o seguinte comando no terminal do seu sistema operacional:
```bash
docker pull esensing/scidb:16.9
```


## Baixando imagem esensing/worcap-mc1:1.0

Para baixar a imagem do container contendo o ambiente de programação Python que será utilizado no minicurso, execute o seguinte comando no terminal do seu sistema operacional:
```bash
docker pull esensing/worcap-mc1:1.0
```


## Verificando a Instalação das Imagens dos Contêineres

```bash
docker images --all
```

A saída deverá apresentar os nomes das seguintes imagens de contêineres:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
esensing/scidb      16.9                648bae1adf4c        2 days ago          10.2GB
```


***Pronto !!!***
