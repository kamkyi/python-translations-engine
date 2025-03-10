import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import json
from po_files_to_single_excel_file import po_to_excel
from single_excel_file_to_po_files import excel_to_po

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translation Management")
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use a modern theme
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('TLabelFrame', font=('Helvetica', 14, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        # PO to Excel section
        self.po_to_excel_frame = ttk.LabelFrame(self.root, text="PO Files to Excel")
        self.po_to_excel_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.po_files_label = ttk.Label(self.po_to_excel_frame, text="Select PO Files:")
        self.po_files_label.pack(anchor="w", padx=10, pady=5)

        self.po_files_button = ttk.Button(self.po_to_excel_frame, text="Browse", command=self.select_po_files)
        self.po_files_button.pack(anchor="w", padx=10, pady=5)

        self.po_files_listbox = tk.Listbox(self.po_to_excel_frame, selectmode="multiple", font=('Helvetica', 12))
        self.po_files_listbox.pack(fill="both", expand="yes", padx=10, pady=5)

        self.excel_file_label = ttk.Label(self.po_to_excel_frame, text="Select Excel File Path:")
        self.excel_file_label.pack(anchor="w", padx=10, pady=5)

        self.excel_file_entry = ttk.Entry(self.po_to_excel_frame, width=50)
        self.excel_file_entry.pack(anchor="w", padx=10, pady=5)

        self.excel_file_button = ttk.Button(self.po_to_excel_frame, text="Browse", command=self.select_excel_file)
        self.excel_file_button.pack(anchor="w", padx=10, pady=5)

        self.convert_po_to_excel_button = ttk.Button(self.po_to_excel_frame, text="Convert", command=self.convert_po_to_excel)
        self.convert_po_to_excel_button.pack(anchor="w", padx=10, pady=5)

        # Excel to PO section
        self.excel_to_po_frame = ttk.LabelFrame(self.root, text="Excel to PO Files")
        self.excel_to_po_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.excel_file_label2 = ttk.Label(self.excel_to_po_frame, text="Select Excel File:")
        self.excel_file_label2.pack(anchor="w", padx=10, pady=5)

        self.excel_file_entry2 = ttk.Entry(self.excel_to_po_frame, width=50)
        self.excel_file_entry2.pack(anchor="w", padx=10, pady=5)

        self.excel_file_button2 = ttk.Button(self.excel_to_po_frame, text="Browse", command=self.select_excel_file2)
        self.excel_file_button2.pack(anchor="w", padx=10, pady=5)

        self.output_dir_label = ttk.Label(self.excel_to_po_frame, text="Select Output Directory:")
        self.output_dir_label.pack(anchor="w", padx=10, pady=5)

        self.output_dir_entry = ttk.Entry(self.excel_to_po_frame, width=50)
        self.output_dir_entry.pack(anchor="w", padx=10, pady=5)

        self.output_dir_button = ttk.Button(self.excel_to_po_frame, text="Browse", command=self.select_output_dir)
        self.output_dir_button.pack(anchor="w", padx=10, pady=5)

        self.convert_excel_to_po_button = tk.Button(self.excel_to_po_frame, text="Convert", command=self.convert_excel_to_po)
        self.convert_excel_to_po_button.pack(anchor="w", padx=10, pady=5)

    def select_po_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PO files", "*.po")])
        self.po_files_listbox.delete(0, tk.END)
        for file_path in file_paths:
            self.po_files_listbox.insert(tk.END, file_path)

    def select_excel_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        self.excel_file_entry.delete(0, tk.END)
        self.excel_file_entry.insert(0, file_path)

    def select_excel_file2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.excel_file_entry2.delete(0, tk.END)
        self.excel_file_entry2.insert(0, file_path)

    def select_output_dir(self):
        directory = filedialog.askdirectory()
        self.output_dir_entry.delete(0, tk.END)
        self.output_dir_entry.insert(0, directory)

    def convert_po_to_excel(self):
        po_file_paths = self.po_files_listbox.get(0, tk.END)
        excel_file_path = self.excel_file_entry.get()
        if not po_file_paths or not excel_file_path:
            messagebox.showerror("Error", "Please select PO files and specify an Excel file path.")
            return
        po_to_excel(po_file_paths, excel_file_path)
        messagebox.showinfo("Success", "PO files have been converted to Excel successfully.")

    def convert_excel_to_po(self):
        excel_file_path = self.excel_file_entry2.get()
        output_directory = self.output_dir_entry.get()
        if not excel_file_path or not output_directory:
            messagebox.showerror("Error", "Please select an Excel file and specify an output directory.")
            return
        excel_to_po(excel_file_path, output_directory)
        messagebox.showinfo("Success", "Excel file has been converted to PO files successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()
