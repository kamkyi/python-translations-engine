import polib
import pandas as pd
import os


def po_to_excel(po_file_paths, excel_file_path):
    all_data = []

    # Iterate through each PO file
    for po_file_path in po_file_paths:
        # Parse the PO file
        po = polib.pofile(po_file_path)
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
    po_file_paths = [
        "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/kh.po",
        "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/bn.po",
        "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/mm.po",
    ]  # List of PO file paths
    excel_file_path = "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/excel_two/multi_two.xlsx"  # Path to the output Excel file
    po_to_excel(po_file_paths, excel_file_path)
