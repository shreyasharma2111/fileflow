import os
import csv
from datetime import datetime  

def generate_summary(valid_files, invalid_files, summary_folder):
    #create summary folder 
    os.makedirs(summary_folder, exist_ok=True)
    
    #make summary file name with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    summary_file = os.path.join(summary_folder, f'summary_{timestamp}.csv')
    
    #write summary data to csv file
    with open(summary_file, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        
        #write header
        writer.writerow(['Filename', 'Status', 'Category', 'Destination'])
        #write valid files
        for file_info in valid_files:
            writer.writerow([file_info[filename],
                             'Valid', 
                             file_info[category], 
                             file_info[destination]
                            ])
        #write invalid files
        for file_info in invalid_files:
            writer.writerow([file_info[filename],
                             'Invalid', 
                             'Quarantine', 
                             file_info[destination]
                            ])
        #separate data from summary
        writer.writerow([])

        #write summary counts
        writer.writerow([f"Total files processed: {len(valid_files) + len(invalid_files)}"])
        writer.writerow([f"Valid files: {len(valid_files)}"])
        writer.writerow([f"Invalid files: {len(invalid_files)}"])  
    
    print(f"Summary: {summary_file}")

    return summary_file