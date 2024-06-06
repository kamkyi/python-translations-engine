```markdown
# Translations Engine

This project provides Python scripts to convert PO files to Excel format and vice versa. There are two versions of the scripts: one for basic conversion and another for handling additional fields and metadata.

## Prerequisites

- Python 3.x
- `pandas` library
- `polib` library
- `xlsxwriter` library (for writing Excel files)

You can install the required libraries using pip:

```bash
pip install pandas polib xlsxwriter
```

## Version 1: Basic Conversion

### PO to Excel

This script converts multiple PO files into a single Excel file, where each PO file's contents are written to a separate sheet.

#### `po_to_excel.py`

1. **Functionality**: This script reads multiple PO files and writes their `msgid` and `msgstr` entries into separate sheets in an Excel file. Each sheet is named after the PO file (without the `.po` extension).

2. **Usage**:
   - Update the `po_file_paths` list with the paths to your PO files.
   - Set the `excel_file_path` to the desired output Excel file path.
   - Run the script.

3. **Example**:
   ```bash
   python3 po_to_excel.py
   ```

### Excel to PO

This script converts an Excel file back into multiple PO files. Each sheet in the Excel file represents a separate PO file.

#### `excel_to_po.py`

1. **Functionality**: This script reads an Excel file where each sheet corresponds to a PO file. It converts each sheet back into a PO file with `msgid` and `msgstr` entries.

2. **Usage**:
   - Set the `excel_file_path` to the path of your Excel file.
   - Set the `output_directory` to the directory where you want to save the generated PO files.
   - Run the script.

3. **Example**:
   ```bash
   python3 excel_to_po.py
   ```

## Version 2: Enhanced Conversion with Additional Fields and Metadata

### PO to Excel

This script converts multiple PO files into a single Excel file with additional fields and metadata.

#### `po_to_excels_two.py`

1. **Functionality**: This script reads multiple PO files and writes their `msgid`, `msgstr`, `comment`, `tcomment`, `occurrences`, and `flags` into separate sheets in an Excel file. Each sheet is named after the PO file (without the `.po` extension).

2. **Usage**:
   - Update the `po_file_paths` list with the paths to your PO files.
   - Set the `excel_file_path` to the desired output Excel file path.
   - Run the script.

3. **Example**:
   ```bash
   python3 po_to_excels_two.py
   ```

### Excel to PO

This script converts an Excel file back into multiple PO files, handling additional fields and metadata.

#### `excels_to_pos_two.py`

1. **Functionality**: This script reads an Excel file where each sheet corresponds to a PO file. It converts each sheet back into a PO file with `msgid`, `msgstr`, `comment`, `tcomment`, `occurrences`, and `flags` entries. It also includes PO file headers.

2. **Usage**:
   - Set the `excel_file_path` to the path of your Excel file.
   - Set the `output_directory` to the directory where you want to save the generated PO files.
   - Run the script.

3. **Example**:
   ```bash
   python3 excels_to_pos_two.py
   ```

## Directory Structure

Assuming your project directory is structured as follows:

```
TRANSLATIONS_ENGINE/
├── po_to_excel.py
├── excel_to_po.py
├── po_to_excels_two.py
├── excels_to_pos_two.py
├── pos/
│   ├── kh.po
│   ├── bn.po
│   ├── mm.po
├── excel/
│   ├── multi.xlsx
│   ├── multi_two.xlsx
├── updated_pos/
├── updated_pos_two/
```

- `po_to_excel.py` and `excel_to_po.py` are the scripts for basic conversion.
- `po_to_excels_two.py` and `excels_to_pos_two.py` are the scripts for enhanced conversion with additional fields and metadata.
- `pos/` is the directory containing your PO files.
- `excel/` is the directory containing your Excel files.
- `updated_pos/` and `updated_pos_two/` are the directories where the output PO files will be saved.

## Notes

- Ensure that the columns in your Excel files match the expected column names (`msgid`, `msgstr`, `comment`, `tcomment`, `occurrences`, `flags`) for the enhanced scripts.
- Modify the example paths in the scripts to match your actual file locations.

## License

This project is licensed under the MIT License.
