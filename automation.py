import os

import shutil

from datetime import datetime

SOURCE_FOLDER = "source"

BACKUP_FOLDER = "backup"

LOG_FILE = "automation.log"

os.makedirs(BACKUP_FOLDER, exist_ok=True)
    
def log_message(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:

        file.write(f"[{timestamp}] {message}\n")

    print(message)


try:

    print("Automation started...")
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    files = os.listdir(SOURCE_FOLDER)

    for file in files:

        source_path = os.path.join(SOURCE_FOLDER, file)

        backup_path = os.path.join(BACKUP_FOLDER, file)

        if os.path.isfile(source_path):

            shutil.copy2(source_path, backup_path)

            log_message(f"Backed up: {file}")

    log_message("Automation completed successfully.")

except Exception as error:

    log_message(f"Automation failed: {error}")
 