FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia


RUN pip install rdkit==2023.03.1
RUN pip install joblib
RUN wget https://github.com/samuelmaina/eos7pw8/raw/main/syba-master.zip
RUN unzip syba-master.zip && cd syba-master
RUN python setup.py install
RUN rm -rf syba-master.zip syba-master

WORKDIR /repo
COPY ./repo
