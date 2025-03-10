# Instructions for setting up the environment:
# 1. Create a virtual environment:
#    python3 -m venv venv
# 2. Activate the virtual environment:
#    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# 3. Install the dependencies:
#    pip install -r requirements.txt

import polib
import pandas as pd
import os
import json


def po_to_excel(po_file_paths, excel_file_path):
    all_data = []

    # Iterate through each PO file
    for po_file_path in po_file_paths:
        if not os.path.exists(po_file_path):
            print(f"File not found: {po_file_path}")
            continue  # Skip this file if it does not exist

        try:
            # Parse the PO file
            po = polib.pofile(po_file_path)
        except IOError as e:
            print(f"Error parsing {po_file_path}: {e}")
            continue  # Skip this file and continue with the next one

        file_name = os.path.basename(po_file_path)

        # Iterate through each entry in the PO file
        for entry in po:
            # Append the data to the list
            all_data.append(
                {
                    "msgid": entry.msgid,
                    "msgstr": entry.msgstr,
                    "comment": entry.comment,
                    "tcomment": entry.tcomment,
                    "occurrences": ", ".join(
                        [f"{occ[0]}:{occ[1]}" for occ in entry.occurrences]
                    ),
                    "flags": ", ".join(entry.flags),
                    "file": file_name,
                }
            )

    # Create a DataFrame from the collected data
    df = pd.DataFrame(
        all_data,
        columns=[
            "msgid",
            "msgstr",
            "comment",
            "tcomment",
            "occurrences",
            "flags",
            "file",
        ],
    )

    # Create an Excel writer
    with pd.ExcelWriter(excel_file_path, engine="xlsxwriter") as writer:
        # Iterate through each language and write data to separate sheets
        for language, data in df.groupby("file"):
            data.drop("file", axis=1, inplace=True)  # Drop 'file' column
            data.to_excel(
                writer, sheet_name=language.split(".")[0], index=False
            )  # Write to sheet


# Example usage
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    
    po_file_paths = [os.path.join(os.path.dirname(__file__), path) for path in config["po_file_paths"]]
    excel_file_path = os.path.join(os.path.dirname(__file__), config["excel_file_path"])
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(excel_file_path), exist_ok=True)
    
    po_to_excel(po_file_paths, excel_file_path)
