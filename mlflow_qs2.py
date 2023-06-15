import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import numpy as np

mlflow.set_tracking_uri("http://aiserver.tzp.haw-landshut.de:5050")


logged_model = 'runs:/81d0408c34ba4392ac6197f35eb9647b/randomForest' #extremely bad model

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
data = np.ones((1,60))
dataDF = pd.DataFrame(data=data)
a = loaded_model.predict(pd.DataFrame(dataDF))
print(a)