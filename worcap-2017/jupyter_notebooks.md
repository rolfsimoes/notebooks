# Preparando ambiente para execução dos Jupyter Notebooks do MC-1
## Baixando o material do MC-1
Baixe o material do MC-1 executando o seguinte comando no terminal:
```
git clone https://github.com/e-sensing/notebooks /tmp/notebooks
```
## Executando o Jupyter Notebook

```
docker run -it --name worcap-mc1 -p 8888:8888 -v /tmp/notebooks/worcap-2017:/home/jovyan/work esensing/worcap-mc1:1.1 start-notebook.sh --NotebookApp.token=''
```

**Pronto !!!** Abra o browser o endereço [http://localhost:8888](http://localhost:8888) no link indicado no terminal
