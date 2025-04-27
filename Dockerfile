FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.03.1
RUN pip install joblib==1.4.2
RUN conda install -c lich -c conda-forge syba=1.0.2.alpha

WORKDIR /repo
COPY . /repo
