import polib
import pandas as pd
import os


def excel_to_multiple_po(excel_file_path, output_directory):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Group by the 'file' column
    grouped = df.groupby("file")

    for file_name, group in grouped:
        # Create a new PO file
        po = polib.POFile()

        for _, row in group.iterrows():
            # Convert values to strings and handle NaNs
            msgid = str(row["msgid"]) if pd.notna(row["msgid"]) else ""
            msgstr = str(row["msgstr"]) if pd.notna(row["msgstr"]) else ""
            comment = str(row["comment"]) if pd.notna(row["comment"]) else ""
            tcomment = str(row["tcomment"]) if pd.notna(row["tcomment"]) else ""
            occurrences = [
                tuple(occ.split(":"))
                for occ in str(row["occurrences"]).split(", ")
                if occ
            ]
            flags = str(row["flags"]).split(", ") if pd.notna(row["flags"]) else []

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
        po_file_path = os.path.join(output_directory, file_name)
        po.save(po_file_path)


# Example usage
if __name__ == "__main__":
    excel_file_path = "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/excel_two/multi.xlsx"
    output_directory = "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/updated_pos"
    excel_to_multiple_po(excel_file_path, output_directory)
