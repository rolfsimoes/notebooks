# Preparando ambiente para execução dos Jupyter Notebooks do MC-1
## Baixando o material
Baixe o material do MC-1 executando o seguinte comando no terminal:
```
git clone https://github.com/e-sensing/notebooks /tmp/notebooks
```
## Executando o Jupyter Notebook

```
docker run -it --name worcap-mc1 -p 8888:8888 -v /tmp/worcap-2017:/home/jovyan/work esensing/worcap-mc1:1.0 start-notebook.sh --NotebookApp.token=''
```

**Pronto !!!** Abra o browser no link indicado no terminal
