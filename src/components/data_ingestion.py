'''data ingestion basically means reading from a database or from some other file locations so initally we need 
 to read the database that is called data ingestion
 it is the phase where raw data is acquired, accessed, collected, 
 and brought into your system in a structured, usable, and reproducible way.'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTrasnformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass # this is a decorator, using this we will be able to directly define our class variable 
# @dataclass is a decorator that transforms a normal class into a dataclass.

class DataIngestionConfig :
    '''It does not perform ingestion itself —
    it stores the settings, paths, and parameters required by the ingestion process.
    It centralizes configuration such as:
    where to fetch data from
    where to store raw data
    file naming conventions
    metadata paths
    temporary storage locations
    logging info'''
    # I will create a artifact folder, and data ingestion will use it to pass all these files in this path  
    train_data_path: str=os.path.join('artifacts',"train.csv") 
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")
    # now the data ingestion knows where to store test,train,raw 


class DataIngestion:
    def __init__(self):
         self.ingestion_config= DataIngestionConfig() # as soon as I call this the 3 paths above will be saved inside this class variable
         # this means that every data ingestion object will have its own config
          
    def initiate_data_ingestion(self):
        # here I will write the code so It could read from the database
         logging.info("Entered the Data ingestion method/component")
         try:
              df = pd.read_csv('notebook/data/stud.csv') 
              logging.info("Read the dataset as dataframe")

              # I will have to make directory for artifacts
              os.makedirs(os.path.dirname(self.ingestion_config.train_data_path ), exist_ok=True)
              df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

              logging.info("Train Test Split initiated")
              train_set, test_set = train_test_split(df, train_size=0.8,random_state=42) 

              train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
              test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

              logging.info("Ingestion is completed")

              return(
                   # I will return these 2 because I will be requiring it for my data transformation so by this data trans.. will be able to grab it 
                   self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path

              )
         except Exception as e:
              raise CustomException(e,sys) 
                    
''' To test it '''
if __name__ =="__main__":
     obj=DataIngestion()
     train_data, test_data = obj.initiate_data_ingestion()

     data_transformation = DataTransformation()
     train_arr , test_arr,_ = data_transformation.initiate_data_transform(train_data,test_data)

     model_trainer = ModelTrainer()
     print(model_trainer.initiate_model_trainer(train_arr,test_arr))