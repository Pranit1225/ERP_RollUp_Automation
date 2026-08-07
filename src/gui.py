from concurrent.futures import thread
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import font

import os

from excel_reader import read_part_numbers

from automation import run_automation

import threading

class RollupApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Amphenol Interconnect India Pvt Ltd")
        self.geometry("650x450")
        self.resizable(False,False)

        self.selected_file = ""

        self.build_ui()

    def build_ui(self):

        padding=10

#! TITLE

        ttk.Label(
            self,
            text="MACOLA ROLL-UP AUTOMATION",
            font=("Segoe UI", 15, "bold"),
        ).pack(pady=(15,20))

#! File Selection Frame

        file_frame = ttk.LabelFrame(
            self,
            text="Excel File",
            padding=10
        )
        file_frame.pack(fill="x", padx=padding)

        self.file_entry = ttk.Entry(file_frame)
        self.file_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        ttk.Button(
            file_frame,
            text="Browse",
            command=self.browse_files
        ).pack(side="right")

#! Selected File

        self.file_label = ttk.Label(
            self,
            text="No File Selected",
            foreground="gray"
        )
        self.file_label.pack(
            anchor="w",
            padx=padding,
            pady=(5, 15)
        )

#! Delay

        delay_frame = ttk.Frame(self)
        delay_frame.pack(fill="x", padx=padding)

        ttk.Label(
            delay_frame,
            text="Start Delay (seconds)",
        ).pack(side="left")

        self.delay_spinbox = ttk.Spinbox(
            delay_frame,
            from_ = 1,
            to = 60,
            width=8
        )
        self.delay_spinbox.pack(side="right")

        self.delay_spinbox.set(5)

#! Instructions

        ttk.Label(
            self,
            text="After clicking START, click inside the ERP textbox before the countdown ends.",
            foreground="blue"
        ).pack(pady=10)

#! Progress Bar

        self.progress = ttk.Progressbar(
            self,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        self.progress.pack(pady=(20, 5))

        self.progress_label = ttk.Label(
            self,
            text="0 / 0"
        )
        self.progress_label.pack()

#! Start

        self.start_button = ttk.Button(
            self,
            text= "START AUTOMATION",
            command=self.start_clicked,
            state="disabled"
        )
        self.start_button.pack(pady=20, ipadx=25, ipady=8)


#!Status

        status_frame = ttk.LabelFrame(
            self,
            text="Status",
            padding=10
        )
        status_frame.pack(fill="x", padx=padding)

        self.status_label = ttk.Label(
            status_frame,
            text="Ready",
        )
        self.status_label.pack(anchor="w")

#!--------------------------

    def browse_files(self):

        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not file_path:
            return

        self.selected_file = file_path

        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

        self.file_label.config(text=os.path.basename(file_path))

        self.start_button.config(state="normal")

#!----------------------------------------

    def start_clicked(self):

        if self.selected_file == "":
            messagebox.showerror(
                "Error",
                "Please select an Excel File"
            )
            return
        
        parts = read_part_numbers(self.selected_file)
        delay = int(self.delay_spinbox.get())
        
        thread = threading.Thread(
            target=run_automation,
            args=(parts, delay),
            daemon=True
        )
        thread.start()


        messagebox.showinfo(
            "Success",
            f"{len(parts)} Part Numbers Loaded."
        )
