## FileFlow:

A command line tool used for validationg, organising and logging files in a shared folder.

## What it does:

This tool scans an input folder and checks each filename against an agreed naming convention. Valid files are sorted in categories in subfolders, while invalid files are moved to a quarantine folder for review. Files that have not been modified in 6 months are archived to keep the workplace tidy. Each action is recoded in a log file, and a summary report is generated.

## Folder Structure:

fileflow/ 

input/ - Drop files here to be processed 

processed/ - Valid files sorted by category 
    
    images/ 
    
    reports/ 
    
    data/ 
    
    general/ 

quarantine/ - Invalid files are moved here 

archive/ - Older processed files are moved here 

logs/ - Log files are saved here 

reports/ - Summary reports are saved here 

fileflow.py - Main script that runs the tool 

validator.py - Checks filenames against the naming rules 

classify.py - Classifies files into categories 

mover.py - Handles moving files between folders 

logs.py - Records actions to the log file 

summary.py - Generates the summary report 

archive.py - Moves older files to the archive folder 

config_loader.py - Loads settings from the config file 

config.json - Settings file 

Dockerfile - Instructions for building the Docker container

run_fileflow.sh - Runs the tool 

reset_demo_data.sh - Resets all folders to a clean state 

backup_reports.sh - Backs up the reports folder


## Filename Naming Convention

For a file to be considered valid it must follow all of these rules:

- The filename must be entirely lowercase
- Words must be separated by underscores
- The filename must start with a date in YYYY-MM-DD format
- The file must have one of the following extensions: .pdf, .csv, .txt, .png, .jpg, .docx, .xlsx, .pptx, .json

Valid example: 2026-04-15_report_summary.pdf
Invalid example: Invoice FINAL.PDF


## Configuration

All settings are stored in config.json. You can change these settings without touching the code.

```json
{
        "input_folder": "input",
            "processed_folder": "processed",
                "quarantine_folder": "quarantine",
                    "archive_folder": "archive",
                        "log_folder": "logs",
                            "summary_folder": "reports",
                                "archive_after_days": 180
}
````
The archive_after_days setting controls how many days a file must be in the processed folder before it gets moved to the archive folder- it is currently set it six months.

## How to Run

Running Locally:

Make sure Python is installed on your machine, then open a terminal in the fileflow folder and run:
```bash
python fileflow.py
```

Running on the Command Line:

You can override the default settings by passing options when you run the tool:

```bash
# use a different input folder
python fileflow.py --input myfolder

# use a different config file
python fileflow.py --config myconfig.json

# set a custom archive threshold in days
python fileflow.py --days 180
```

Running With the Bash Script:

A bash script is included that runs the tool with one command:

```bash
./run_fileflow.sh


Running in Docker:
First build the Docker image:

```bash
docker build -t fileflow .
```

Then run the container, replacing YourName with your Windows username:

```bash
MSYS_NO_PATHCONV=1 docker run -it --rm \
    -v "C:/Users/YourName/Documents/fileflow/input:/app/input" \
    -v "C:/Users/YourName/Documents/fileflow/processed:/app/processed" \
    -v "C:/Users/YourName/Documents/fileflow/quarantine:/app/quarantine" \
    -v "C:/Users/YourName/Documents/fileflow/logs:/app/logs" \
    -v "C:/Users/YourName/Documents/fileflow/reports:/app/reports" \
    fileflow
```

## Other Bash Scripts:

reset_demo_data.sh :

Clears all folders back to a clean empty state. Useful for testing the tool repeatedly without manually deleting files.

```bash
/reset_demo_data.sh
```
backup_reports.sh :

Creates a timestamped backup of the reports folder so that generated reports are never lost.

 ```bash
./backup_reports.sh
```

## How AI Was Used

AI tools were used throughout this project to support development. This included help with drafting the project backlog and acceptance criteria, suggesting the initial project structure, generating file classification rules, debugging errors in the code, and improving this README. A full record of the prompts used can be found in ai_log.txt.

## Author
Shreya Sharma
