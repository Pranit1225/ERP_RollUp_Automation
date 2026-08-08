from concurrent.futures import thread
import tkinter as tk
from tkinter import ttk, filedialog

import os
from excel_reader import read_part_numbers
from automation import run_automation
import threading

class RollupApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Amphenol Interconnect India Pvt Ltd")
        self.geometry("650x650")
        self.resizable(False,False)

        self.selected_file = ""
        self.parts=[]

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

#?-------------------
        self.status_label = ttk.Label(
            status_frame,
            text="Ready",
        )
        self.status_label.pack(anchor="w", pady=2)
#?--------------------
        self.current_part_label = ttk.Label(
            status_frame,
            text="Current Part : "
        )
        self.current_part_label.pack(anchor="w", pady=2)
#?--------------------

        self.records_label = ttk.Label(
            status_frame,
            text="Records : 0/0"
        )
        self.current_part_label.pack(anchor="w", pady=2)

#!--------------------------

    def browse_files(self):

        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not file_path:
            return

        try:
            parts = read_part_numbers(file_path)
        except Exception as error:
            self.status_label.config(text="Unable to read Excel File")
            print(f"Excel Error : {error}")

            return
        if not parts:
            self.status_label.config(text="No Entries Found.")

            return
    
        self.selected_file = file_path
        self.parts = parts

#?Display Selected File
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

        self.file_label.config(text=f"Selected {os.path.basename(file_path)}")

#? Update Status

        self.status_label.config(text=f"Status : {len(parts)} Entries Loaded")
        self.current_part_label.config(text="Current Part : ")
        self.records_label.config(text=f"Records : 0 / {len(parts)}")

#? Reset Progress
        self.progress["maximum"] = len(parts)
        self.progress["value"] = 0
        self.progress_label.config( text=f"0 / {len(parts)}")

        self.start_button.config(state="normal")
#!----------------------------------------
#! On CLICKING

    def start_clicked(self):
        
        if not self.parts:
            self.status_label.config(
            text="Status : Please select an Excel file."
        )
            return
        try:
            delay = int(self.delay_spinbox.get())
        except ValueError:
            self.status_label.config(
                text="Invalid delay value."
            )
            return

        # Reset progress
        self.progress["value"] = 0
        self.progress_label.config(text=f"0 / {len(self.parts)}")
        self.records_label.config(text=f"Records : 0 / {len(self.parts)}")
        self.current_part_label.config(text="Current Part : -")

       # parts = read_part_numbers(self.selected_file)
        
        threading.Thread(
                target=run_automation,
                args=(
                    self.parts,
                    delay,
                    self.on_countdown,
                    self.on_progress,
                    self.on_complete
                ),
                daemon=True
            ).start()
        

        self.start_button.config(state="disabled")

#! STATUS PROGRESS

    def on_countdown(self, seconds):

        self.after(
            0,
            lambda: self.status_label.config(text=f"Status : Automation Begins in {seconds} seconds...")
        )

    def on_progress(self, current, total, part):

        def update():
            self.progress["maximum"] = total
            self.progress["value"] = current

            self. progress_label.config(text=f"{current} / {total}")
            self.records_label.config(text=f"Records : {current} / {total}")
            self.cuurent_label.config(text=f"Current Part : {part}")
            self.status_label.config(text="Running...")

        self.after(0, update)

    def on_complete(self, total):

        def update():
            self.progress["maximum"] = total
            self.progress["value"] = total
            
            self. progress_label.config(text=f"{total} / {total}")
            self.records_label.config(text=f"Records : {total} / {total}")
            self.current_part_label.config(text="Current Part : ")
            self.status_label.config(text=f"Completed. Processed {total} Records")
            self.start_button.config(state="normal")

        self.after(0, update)

