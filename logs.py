import os
from datetime import datetime

def logaction(message, log_folder):
    #create log folder if it doesn't exist
    os.makedirs(log_folder, exist_ok=True)
    
    #construct log file path
    log_file = os.path.join(log_folder, 'fileflow.log')
    
    #get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #write log message to file
    with open(log_file, 'a') as log_file:
        log_file.write(f'{timestamp} - {message}\n')
    

