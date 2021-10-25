FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c rdkit rdkit=2020.03
RUN conda install -c lich syba

WORKDIR /repo
COPY ./repo
