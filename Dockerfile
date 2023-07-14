FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2023.03.1
RUN pip install joblib
RUN conda install model/checkpoints/syba-1.0.2.alpha-py_0.tar.bz2

WORKDIR /repo
COPY ./repo
