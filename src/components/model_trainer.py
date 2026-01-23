# how many models i want to use , confusion matrix everything
''' try every model and see which performs better'''

import os
import sys

from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

# for every component we need to create its config file also
@dataclass
class ModelTrainerConfig: # this will basically give input whatever I require wrt model training
     trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
     def __init__ (self):
          self.model_trainer_config= ModelTrainerConfig()

     def initiate_model_trainer(self,train_array,test_array):
          try:
               logging.info(f"Splitting training and test input data")
               X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
                ) 
               # After this I will create a dictionary of models
               models={
                    "Random Forest" : RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boost": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegression(),
                    "K Neighbour Regression": KNeighborsRegressor(),
                    "KGB":KNeighborsRegressor(),
                    "CatBoost Regressor": CatBoostRegressor(verbose=False),
                    "Ada Boost Regressor": AdaBoostRegressor()
               }
                # try hyperparameter tuning
               model_report:dict= evaluate_model(X_train=X_train,y_train=y_train,X_test = X_test,y_test = y_test,models=models)

               # To get best model score from dictionary
               best_model_score = max(sorted(model_report.values()))

              # To get best model score report from dictionary
               best_model_name= list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
               ]

               best_model = models[best_model_name]

               if(best_model_score < 0.6):
                    raise CustomException("No Best model found")
               
               logging.info(f"Best model found on both training and testing data")

               save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model
               )

               predicted=best_model.predict(X_test)

               r2_scores = r2_score(y_test,predicted)
               return r2_scores


          except Exception as e:
               raise CustomException(e,sys)
     
'''
pickle file is created so that the trained model is saved so you can test it without training it again
'''