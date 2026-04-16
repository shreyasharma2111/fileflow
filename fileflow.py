import os
from unicodedata import category
from validator import validatefilename
from mover import movefile
from logs import logaction
from config_loader import loadconfig
from classify import classify_file

input_folder = 'input'
processed_folder = 'processed'
quarantine_folder = 'quarantine'
log_folder = 'logs'

def checkfolder(folder):
    #check if folder exists
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return []

    files = []
    #go through everything in the folder
    for filename in os.listdir(folder):
        #build whole path to file
        fullpath = os.path.join(folder, filename)

        #check if it's a file and not a folder
        if os.path.isfile(fullpath):
            files.append(fullpath)
    return files


def processfiles(files, config):

    #get folder paths from config
    processed_folder = config['processed_folder']
    quarantine_folder = config['quarantine_folder']
    log_folder = config['log_folder']
    categoroies = config['categories']


    valid = 0
    invalid = 0
    for filepath in files:
        #get only the name
        filename = os.path.basename(filepath)

        #to stop code from crashing
        try:
            #check if name is valid
            if validatefilename(filename):
                #classify file into category
                category = classify_file(filename, categoroies)
                #build new destination folder
                destination_folder = os.path.join(processed_folder, category)
                #yes then move it to processed folder
                newpath = movefile(filepath, destination_folder)
                #log the action
                logaction(f'VALID: {filename} moved to {newpath}', log_folder)
                print(f"Valid file: {filename} moved to {category}")
                #increment valid counter
                valid += 1
            else:
                #no then move it to quarantine folder
                newpath = movefile(filepath, quarantine_folder)
                #log the action
                logaction(f'INVALID: {filename} moved to {newpath}', log_folder)
                print(f"Invalid file: {filename} moved to quarantine")
                #increment invalid counter
                invalid += 1

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logaction(f"ERROR: {filename} - {str(e)}", log_folder)


    print(f'Total files processed: {valid + invalid}')
    print(f'Valid files: {valid}')
    print(f'Invalid files: {invalid}')
    print(f'---Summary---')

if __name__ == '__main__':
    #load config
    try:
        config = loadconfig()
        print(f"Config has been loaded")
    except Exception as e:
        print(f"Error loading config: {str(e)}")
        exit()

    input_folder = config.get('input_folder')
    files = checkfolder(input_folder)
    print(f'Found {len(files)} files in {input_folder} folder.')
    processfiles(files, config)
    print('Processing complete')