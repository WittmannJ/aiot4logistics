FROM tensorflow/tensorflow:2.11.0-gpu-jupyter

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

RUN apt-get update
RUN apt-get -y install htop
RUN apt-get -y install libgit2-dev


# install auto-sklearn
RUN apt-get -y install build-essential swig python3-dev
RUN apt-get -y install libcairo2-dev pkg-config python3-dev

RUN python -m pip install --upgrade pip


COPY myrequirements.txt myrequirements.txt
RUN python -m pip install -r myrequirements.txt
RUN python -m pip install auto-sklearn

# # install the other dependencies i need for my code
# RUN python -m pip install pandas
# RUN python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
# RUN python -m pip install scikit-learn
# RUN python -m pip install influxdb
# RUN python -m pip install seaborn
# RUN python -m pip install autopep8
# RUN python -m pip install paho-mqtt
# RUN python -m pip install mlflow
# RUN python -m pip install dvc



ENV SHELL /bin/bash