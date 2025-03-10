# Translation Management

This project provides tools for converting PO files to a single Excel file and vice versa. It also includes a graphical user interface (GUI) for ease of use.

## Setup

### 1. Create a virtual environment

```sh
python3 -m venv venv
```

### 2. Activate the virtual environment

On Linux/macOS:

```sh
source venv/bin/activate
```

On Windows:

```sh
venv\Scripts\activate
```

### 3. Install the dependencies

```sh
pip install -r requirements.txt
```

### 4. Install `tkinter`

On Ubuntu/Debian-based systems:

```sh
sudo apt-get update
sudo apt-get install python3-tk
```

On Fedora:

```sh
sudo dnf install python3-tkinter
```

On Windows and macOS, `tkinter` is included with the standard Python installation.

## Running the UI Application

To run the graphical user interface (GUI) application, execute the following command:

```sh
python ui.py
```

This will open a window where you can select PO files, specify an Excel file path, and convert between PO and Excel files using a graphical interface.

## Usage

### PO Files to Excel

1. Click on the "Browse" button to select PO files.
2. Click on the "Browse" button to specify the path for the Excel file.
3. Click on the "Convert" button to convert the selected PO files to an Excel file.

### Excel to PO Files

1. Click on the "Browse" button to select an Excel file.
2. Click on the "Browse" button to specify the output directory for the PO files.
3. Click on the "Convert" button to convert the selected Excel file to PO files.

## Example Usage in Scripts

### PO Files to Excel

```python
# filepath: /home/kamkyi/python-translations-engine/po_files_to_single_excel_file.py
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    po_file_paths = [os.path.join(os.path.dirname(__file__), path) for path in config["po_file_paths"]]
    excel_file_path = os.path.join(os.path.dirname(__file__), config["excel_file_path"])

    # Ensure the directory exists
    os.makedirs(os.path.dirname(excel_file_path), exist_ok=True)

    po_to_excel(po_file_paths, excel_file_path)
```

### Excel to PO Files

```python
# filepath: /home/kamkyi/python-translations-engine/single_excel_file_to_po_files.py
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    excel_file_path = os.path.join(os.path.dirname(__file__), config["excel_file_path"])
    output_directory = os.path.join(os.path.dirname(__file__), "updated_po_files")

    if not os.path.exists(excel_file_path):
        print(f"Excel file not found: {excel_file_path}")
    else:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        excel_to_po(excel_file_path, output_directory)
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
├── po_files_to_single_excel_file.py
├── single_excel_file_to_po_files.py
├── config.json
├── po_files/
│   ├── kh.po
│   ├── bn.po
│   ├── mm.po
├── excel/
│   ├── multiple_translations.xlsx
├── updated_po_files/
```

- `po_files_to_single_excel.py` and `excel_to_po_files.py` are the scripts for basic conversion.
- `po_to_excels_two.py` and `single_excel_to_po_files.py` are the scripts for enhanced conversion with additional fields and metadata.
- `config.json` is the configuration file containing the relative paths.
- `po_files/` is the directory containing your PO files.
- `excel/` is the directory containing your Excel files and also it's the source directory to pick the excel and convert to multiple-po files
- `updated_po_files/` is the directory where the output PO files will be saved.

## Notes

- Ensure that the columns in your Excel files match the expected column names (`msgid`, `msgstr`, `comment`, `tcomment`, `occurrences`, `flags`) for the enhanced scripts.
- Modify the example paths in the `config.json` file to match your actual file locations.

## License

This project is licensed under the MIT License.
