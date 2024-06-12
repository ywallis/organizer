import os
import shutil
import json
import re
from datetime import datetime

with open("extensions.json", "r") as extension_file:
    file_extensions = json.load(extension_file)


def is_valid_date_filename(filename):
    """ Function takes a string as an input, and checks if the string begins by a date in YYY_MM_DD format.
    If yes, the function returns True, else, False"""

    # Define the regex pattern for YYYY_MM_DD at the start of the string
    pattern = r'^\d{4}_\d{2}_\d{2}'

    # Use re.match to check if the pattern matches at the start of the filename
    if re.match(pattern, filename):
        return True
    else:
        return False


def organize_core(path):
    """Function takes in an os filepath as a string, and uses os
    and shutil modules to organize all files in that directory, depending on their file extensions.
    A list of file extensions must be provided."""

    with os.scandir(path) as files:
        for file in files:
            if not file.is_dir():
                file_creation_timestamp = os.path.getctime(path + "/" + file.name)
                file_creation_date = datetime.fromtimestamp(file_creation_timestamp).strftime("%Y_%m_%d")
                if is_valid_date_filename(file.name):
                    new_name = file.name
                else:
                    new_name = f"{file_creation_date}_{file.name}"

                filename, extension = os.path.splitext(file.name)
                extension = extension[1:]
                file_type = file_extensions.get(extension, "Others")

                if os.path.exists(path + "/" + file_type):
                    shutil.move(path + "/" + file.name, path + "/" + file_type + "/" + new_name)
                else:
                    os.makedirs(path + "/" + file_type)
                    shutil.move(path + "/" + file.name, path + "/" + file_type + "/" + new_name)



