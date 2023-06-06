FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c rdkit -c lich syba


WORKDIR /repo
COPY ./repo
