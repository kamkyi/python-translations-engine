# Python Translations Engine

## Setup Instructions

1. Create a virtual environment:

   ```sh
   python3 -m venv venv
   ```

2. Activate the virtual environment:

   ```sh
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Convert PO Files to a Single Excel File

To convert PO files located in the `po_files` directory to a single Excel file in the `excel` directory, run:

```sh
python po_files_to_single_excel_file.py
```

### Convert a Single Excel File to PO Files

To convert an Excel file located in the `excel` directory to PO files in the `updated_po_files` directory, run:

```sh
python single_excel_file_to_po_files.py
```

## Configuration

The paths for the PO files and the Excel file are specified in the `config.json` file:

```json
{
  "po_file_paths": ["po_files/kh.po", "po_files/bn.po", "po_files/mm.po"],
  "excel_file_path": "excel/multiple_translations.xlsx"
}
```

## Version 1: Basic Conversion

### PO to Excel

This script converts multiple PO files into a single Excel file, where each PO file's contents are written to a separate sheet.

#### `po_to_excel.py`

1. **Functionality**: This script reads multiple PO files and writes their `msgid` and `msgstr` entries into separate sheets in an Excel file. Each sheet is named after the PO file (without the `.po` extension).

2. **Usage**:

   - Update the `config.json` file with the relative paths to your PO files and the desired output Excel file path.
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

   - Update the `config.json` file with the relative paths to your PO files and the desired output Excel file path.
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
├── config.json
├── po_files/
│   ├── kh.po
│   ├── bn.po
│   ├── mm.po
├── excel/
│   ├── multi.xlsx
├── excel_two/
│   ├── multi_two.xlsx
├── updated_po_files/
├── updated_po_files_two/
```

- `po_to_excel.py` and `excel_to_po.py` are the scripts for basic conversion.
- `po_to_excels_two.py` and `excels_to_pos_two.py` are the scripts for enhanced conversion with additional fields and metadata.
- `config.json` is the configuration file containing the relative paths.
- `po_files/` is the directory containing your PO files.
- `excel/` is the directory containing your Excel files.
- `excel_two/` is the directory containing your enhanced Excel files.
- `updated_po_files/` and `updated_po_files_two/` are the directories where the output PO files will be saved.

## Notes

- Ensure that the columns in your Excel files match the expected column names (`msgid`, `msgstr`, `comment`, `tcomment`, `occurrences`, `flags`) for the enhanced scripts.
- Modify the example paths in the `config.json` file to match your actual file locations.

## License

This project is licensed under the MIT License.
