!/usr/bin/env bash

#make a backup folder
mkdir -p backup

#create a timestamped backup name
backup_name="backup_$(date +%Y%m%d_%H%M%S)"

#copy everything from the summary folder to the backup folder
cp -r summary "$backup_name"

echo "Backup of summary reports created: $backup_name"
