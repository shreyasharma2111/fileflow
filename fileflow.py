import os
from validator import validatefilename
from mover import movefile
from logs import logaction

input_folder = 'input'
processed_folder = 'processed'
quarantine_folder = 'quarantine'
log_folder = 'logs'

def checkfolder(folder):
    files = []
    #go through everything in the folder
    for filename in os.listdir(folder):
        #build whole path to file
        fullpath = os.path.join(folder, filename)

        #check if it's a file and not a folder
        if os.path.isfile(fullpath):
            files.append(fullpath)
    return files


def processfiles(files):
    valid = 0
    invalid = 0
    for filepath in files:
        #get only the name
        filename = os.path.basename(filepath)

        #check if name is valid
        if validatefilename(filename):
            #yes then move it to processed folder
            newpath = movefile(filepath, processed_folder)
            #log the action
            logaction(f'VALID: {filename} moved to {newpath}', log_folder)
            #increment valid counter
            valid += 1
        else:
            #no then move it to quarantine folder
            newpath = movefile(filepath, quarantine_folder)
            #log the action
            logaction(f'INVALID: {filename} moved to {newpath}', log_folder)
            #increment invalid counter
            invalid += 1


            print(f'---Summary---')
            print(f'Total files processed: {valid + invalid}')
            print(f'Valid files: {valid}')
            print(f'Invalid files: {invalid}')

if __name__ == '__main__':
    files = checkfolder(input_folder)
    print(f'Found {len(files)} files in {input_folder} folder.')
    processfiles(files)
    print('Processing complete')