import os
from unicodedata import category
from validator import validatefilename
from mover import movefile
from logs import logaction
from config_loader import loadconfig
from classify import classify_file
from summary import generate_summary
from archive import archived_files

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
    summary_folder = config['summary_folder']
    from archive import archived_files

    valid = 0
    valid_files = []
    invalid = 0
    invalid_files = []

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
                #duplicate file name check
                final_destination = os.path.join(destination_folder, filename)
                if os.path.exists(final_destination):
                    base, ext = os.path.splittext(filename)
                    count = 1
                    while os.path.exists(os.path.join(destination_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    filename = f"{base}_{counter}{ext}"
                #valid name then move it to processed folder
                newpath = movefile(filepath, destination_folder)
                #log the action
                logaction(f'VALID: {filename} moved to {newpath}', log_folder)
                print(f"Valid file: {filename} moved to {category}")
                #increment valid counter
                valid += 1
                #add to valid files list for summary
                valid_files.append({
                    'filename': filename,
                    'category': category,
                    'destination': newpath
                }) 

            else:
                #duplicate file name check for quarantine
                final_destination = os.path.join(quarantine_folder, filename)
                if os.path.exists(final_destination):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(os.path.join(quarantine_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    filename = f"{base}_{counter}{ext}"
                #not valid then move it to quarantine folder
                newpath = movefile(filepath, quarantine_folder)
                #log the action
                logaction(f'INVALID: {filename} moved to {newpath}', log_folder)
                print(f"Invalid file: {filename} moved to quarantine")
                #increment invalid counter
                invalid += 1
                #add to invalid files list for summary
                invalid_files.append({
                    'filename': filename,
                    'destination': newpath
                })

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logaction(f"ERROR: {filename} - {str(e)}", log_folder)


    print(f'---Summary---')
    print(f'Total files processed: {valid + invalid}')
    print(f'Valid files: {valid}')
    print(f'Invalid files: {invalid}')
    print(f'Files archived: check archive folder')
    #generate summary report
    summary_file = generate_summary(valid_files, invalid_files, summary_folder)

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
    print(f'Processing complete')
    print(f"Checking for old files to archive...")
    archived_files(
        config['processed_folder'], 
        config['archive_folder'], 
        config['log_folder'],
        config['archive_after_days']
        
    )
