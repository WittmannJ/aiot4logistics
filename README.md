# aiot4logistics

this project requires this packages

RUN python -m pip install auto-sklearn

# install the other dependencies i need for my code
#RUN python -m pip install pygit2
RUN python -m pip install pandas
RUN python -m pip install scipy matplotlib ipython jupyter pandas sympy nose
RUN python -m pip install scikit-learn
RUN python -m pip install influxdb
RUN python -m pip install seaborn
RUN python -m pip install autopep8
RUN python -m pip install paho-mqtt
RUN python -m pip install mlflow
#RUN python -m pip install dvc !!error does not install 

-> src/diff.h:33:10: fatal error: git2.h: No such file or directory
     33 | #include <git2.h>
        |          ^~~~~~~~
  compilation terminated.
  error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
  ----------------------------------------
  ERROR: Failed building wheel for pygit2
Successfully built antlr4-python3-runtime nanotime
Failed to build pygit2
ERROR: Could not build wheels for pygit2 which use PEP 517 and cannot be installed directly


RUN python -m pip install everywhereml>=0.2.9