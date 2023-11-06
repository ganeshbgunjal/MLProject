import logging
import os 
from datetime import datetime

'''
 Logging is a means of tracking events that happen when some software runs. The software developer
 adds logging calls to their code to indicate that certain events have occurred. An event is described 
 by a descriptive message which can optionally contain variable data (i.e. data that is potentially
 different for each occurrence of the event).
'''

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
)

# if __name__ == "__main__": 
#     logging.info("Logging has started")

# above line will show up exception and we do it for understanding. it has no need more