'''everything that happens you should be able to log it into a file so we'll we able to track it, even the 
exceptions we can log into custom files 
Whenever I will get an exception I will take it logging it with our logger file and use logging.info to
put it inside logger file'''


import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # month day year hour minutes seconds
logs_path=os.path.join(os.getcwd(),"logs", LOG_FILE)  # whatever logs will be created it will be respect to current working directory. a log folder will be created and every file will start with logs along with that whatever file name is coming
os.makedirs(logs_path,exist_ok=True)  # this says even though there is a folder keep on appending the file inside it

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# now whenever you want to overwrite the funcitonality of logging you have to change config

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # so in case of info only I am going to print these messages

    # in case of logging or logging.info or any print message it is going to create this file path , this format


)
''' 
# THis is just to check
if __name__=="__main__":
    logging.info(" Logging has started")
'''