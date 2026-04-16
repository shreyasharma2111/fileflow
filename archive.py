import os
import shutil
from datetime import datetime
from logs import logaction

def archived_files(processed_folder, archive_folder, log_folder, archive_after_days):

    #check if folder exisits
    os.makedirs(archive_folder, exist_ok=True)

    archived_count = 0

    now = datetime.now()

    for root, dirs, files in os.walk(processed_folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            #get last modified time
            modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            #calculate how long it's been since modified
            days_since_modified = (now - modified_time).days
            #if it's been more than 6 months, move to archive
            if days_since_modified >= 180: 
                #build new destination path
                destination = os.path.join(archive_folder, filename)
                #duplicate file name check
                if os.path.exists(destination):
                    base, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(os.path.join(archive_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    destination = os.path.join(archive_folder, f"{base}_{counter}{ext}")

                #move file to archive
                shutil.move(filepath, destination)
                #log the action
                logaction(f'ARCHIVED: {filename} moved to {destination}', log_folder)
                print(f"Archived file: {filename} moved to archive")
                archived_count += 1
    print(f"Total archived files: {archived_count}")

    return archived_count
