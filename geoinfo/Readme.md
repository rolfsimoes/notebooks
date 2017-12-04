# Short Course - Big Earth Observation Data Analytics

<p style="font-weight: bold;text-align: right">XVIII Brazilian Symposium on Geoinformatics</p>
<p style="font-weight: bold;text-align: right">December 04th to 06th, Salvador, BA, Brazil</p>

This document explains how to prepare the computational environment for the course.

## Installing Docker

Install [Docker](https://www.docker.com) in your computer.

If you have Linux Ubuntu 16.04, follow the step-by-step guide [here](https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-16-04-pt), otherwise, follow the instructions in [Docker's site](https://www.docker.com/community-edition).

After installing Docker, follow the instructions to install the image containers that we have prepared for the short-course.


## Downloading the Docker Image `esensing/scidb:16.9`

In order to download the container image with SciDB prepared for the course, type the following command in your terminal:
```bash
docker pull esensing/scidb:16.9
```


## Downloading the Docker Image `esensing/geoinfo:1.0`

In order to download the container image with the Python environment prepared for the course, type the following command in the terminal:
```bash
docker pull esensing/geoinfo:1.0
```


## Verify the Installed Containers

```bash
docker images --all
```

The output from the above command should display names such as:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
esensing/scidb      16.9                648bae1adf4c        2 days ago          10.2GB
esensing/geoinfo    1.1                 7a23cb3a4845        9 minutes ago       3.16GB
```


***Finished !!!***