FROM tensorflow/tensorflow:latest-gpu-jupyter

# # System requirements
# RUN apt-get update && apt-get install -y \
#   build-essential \
#   curl \
#   python3-pip \
#   swig \
#   && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 tzpulski \
    && useradd --home-dir /home/tzpulski --create-home --uid 1000 \
    --gid 1000 --shell /bin/sh --skel /dev/null tzpulski

ARG USERNAME=tzpulski

RUN mkdir -p /home/$USERNAME/.vscode-server/extensions \
        /home/$USERNAME/.vscode-server-insiders/extensions \
    && chown -R $USERNAME \
        /home/$USERNAME/.vscode-server \
        /home/$USERNAME/.vscode-server-insiders

# install auto-sklearn
RUN apt-get -y install build-essential swig python3-dev
RUN python -m pip install auto-sklearn

# install the other dependencies i need for my code
RUN python -m pip install pandas
RUN python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
RUN python -m pip install scikit-learn
RUN python -m pip install influxdb
RUN python -m pip install seaborn
RUN python -m pip install autopep8
RUN python -m pip install paho-mqtt
RUN python -m pip install mlflow
RUN python -m pip install dvc



ENV SHELL /bin/bash