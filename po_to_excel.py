import polib
import pandas as pd
import os


def multiple_po_to_excel(po_file_paths, excel_file_path):
    all_data = []

    for po_file_path in po_file_paths:
        # Parse the PO file
        po = polib.pofile(po_file_path)
        file_name = os.path.basename(po_file_path)

        # Prepare data for the DataFrame
        for entry in po:
            all_data.append(
                {
                    "file": file_name,
                    "msgid": entry.msgid,
                    "msgstr": entry.msgstr,
                    "comment": entry.comment,
                    "tcomment": entry.tcomment,
                    "occurrences": ", ".join(
                        [f"{occ[0]}:{occ[1]}" for occ in entry.occurrences]
                    ),
                    "flags": ", ".join(entry.flags),
                }
            )

    # Create a DataFrame
    df = pd.DataFrame(
        all_data,
        columns=[
            "file",
            "msgid",
            "msgstr",
            "comment",
            "tcomment",
            "occurrences",
            "flags",
        ],
    )

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)


# Example usage
po_file_paths = [
    "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/kh.po",
    "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/bn.po",
    "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/source_pos/mm.po",
]
excel_file_path = "/home/kamkyi/Desktop/TRANSLATIONS_ENGINE/excel/multi.xlsx"
multiple_po_to_excel(po_file_paths, excel_file_path)
