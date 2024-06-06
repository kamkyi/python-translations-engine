import pandas as pd
import polib
import os


def excel_to_po(excel_file_path, output_directory):
    # Read the Excel file
    df = pd.read_excel(excel_file_path, sheet_name=None)

    # Debug: Print sheet names and first few rows of each sheet
    for sheet_name in df.keys():
        print(f"Sheet name: {sheet_name}")
        print(df[sheet_name].head())

    # Iterate over each sheet (language)
    for language, data in df.items():
        # Initialize a new PO file
        po = polib.POFile()

        # Set the header metadata
        po.metadata = {
            "Project-Id-Version": "",
            "POT-Creation-Date": "",
            "PO-Revision-Date": "2024-06-06 15:40+0700",
            "Last-Translator": "",
            "Language-Team": "",
            "Language": language,
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=UTF-8",
            "Content-Transfer-Encoding": "8bit",
            "X-Generator": "Poedit 3.4.3",
            "X-Poedit-Basepath": ".",
        }

        # Check if the required columns exist
        required_columns = ["msgid", "msgstr"]
        for col in required_columns:
            if col not in data.columns:
                print(f"Error: Missing required column '{col}' in sheet '{language}'")
                continue  # Skip this sheet if required column is missing

        # Iterate over each row in the sheet
        for _, row in data.iterrows():
            # Extract values and handle NaNs
            msgid = str(row["msgid"]) if pd.notna(row["msgid"]) else ""
            msgstr = str(row["msgstr"]) if pd.notna(row["msgstr"]) else ""
            comment = (
                str(row["comment"])
                if "comment" in row and pd.notna(row["comment"])
                else ""
            )
            tcomment = (
                str(row["tcomment"])
                if "tcomment" in row and pd.notna(row["tcomment"])
                else ""
            )
            occurrences = []
            if "occurrences" in row and pd.notna(row["occurrences"]):
                for occ in row["occurrences"].split(", "):
                    parts = occ.split(":")
                    if len(parts) == 2:
                        occurrences.append(tuple(parts))

            flags = (
                str(row["flags"]).split(", ")
                if "flags" in row and pd.notna(row["flags"])
                else []
            )

            # Create a new PO entry
            entry = polib.POEntry(
                msgid=msgid,
                msgstr=msgstr,
                comment=comment,
                tcomment=tcomment,
                occurrences=occurrences,
                flags=flags,
            )
            po.append(entry)

        # Save the PO file
        po_file_path = os.path.join(output_directory, f"{language}.po")
        po.save(po_file_path)


# Example usage
if __name__ == "__main__":
    excel_file_path = (
        "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/excel_two/multi_two.xlsx"
    )
    output_directory = "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/updated_pos_two"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    excel_to_po(excel_file_path, output_directory)
