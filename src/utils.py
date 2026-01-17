''' any functionality i am writing in common way that i am going to use throughout
 my function i am going to write it here. Lets say i want to read a database, i create my mongodb client over here
  I will try to call this util in componenets '''

import os
import sys

import numpy as np
import pandas as pd
import dill

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:

        report={}

        for i in range (len(list(models))):
            model = list(models.values())[i]
            
            model.fit(X_train,y_train)

            y_train_predict = model.predict(X_train)

            y_test_predict = model.predict(X_test)

            train_model_score = r2_score(y_train,y_train_predict)

            test_model_score = r2_score(y_test,y_test_predict)

            report[list(models.keys())[i]] = test_model_score
            
            return report
        
    except Exception as e:
        raise CustomException(e,sys)

