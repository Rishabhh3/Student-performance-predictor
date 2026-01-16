''' any functionality i am writing in common way that i am going to use throughout
 my function i am going to write it here. Lets say i want to read a database, i create my mongodb client over here
  I will try to call this util in componenets '''

import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise(e,sys)