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
        self.geometry("650x420")
        self.resizable(False,False)

        self.selected_file = ""
        self.parts=[]
        self.stop_event = threading.Event()

        self.build_ui()

    def build_ui(self):

        padding=10

#! TITLE

        ttk.Label(
            self,
            text="MACOLA ROLL-UP AUTOMATION",
            font=("Segoe UI", 15, "bold"),
        ).pack(pady=(5,10))

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
            command=self.browse_files,
            cursor="hand2"
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

        # delay_frame = ttk.Frame(self)
        # delay_frame.pack(fill="x", padx=padding)

        # ttk.Label(
        #     delay_frame,
        #     text="Start Delay (seconds)",
        # ).pack(side="left")

        # self.delay_spinbox = ttk.Spinbox(
        #     delay_frame,
        #     from_ = 1,
        #     to = 60,
        #     width=8
        # )
        # self.delay_spinbox.pack(side="right")

        # self.delay_spinbox.set(5) 

        # action_delay_frame = ttk.Frame(self)
        # action_delay_frame.pack(fill="x", padx=padding,pady=(0,5))

        # ttk.Label(
        #     action_delay_frame,
        #     text="Validation Delay (seconds)"
        # ).pack(side="left", pady=10)

        # self.action_delay_values = (
        #     "0.1",
        #     "0.5",
        #     "1.0",
        #     "1.5",
        #     "2.0",
        #     "2.5",
        #     "3.0",
        #     "3.5",
        #     "4.0",
        #     "4.5",
        #     "5.0",
        # )

        # self.action_delay_spinbox = ttk.Spinbox(
        #     action_delay_frame,
        #     values=self.action_delay_values,
        #     width=8,
        #     state="readonly"
        # )
        # self.action_delay_spinbox.pack(side="right")

        # self.action_delay_spinbox.set("0.1")
        
#! Instructions

        ttk.Label(
            self,
            text="After clicking START, click inside the ERP textbox before the 7 Seconds countdown ends.",
            foreground="blue"
        ).pack(pady=10)

#! Progress Bar

        self.progress = ttk.Progressbar(
            self,
            orient="horizontal",
            length=500,
            mode="determinate"
        )
        self.progress.pack()#pady=(20, 5))

        self.progress_label = ttk.Label(
            self,
            text="0 / 0"
        )
        self.progress_label.pack()

#! Start & Stop ---------------------------------

        button_frame = ttk. Frame()
        button_frame.pack(pady=(15,15))

        self.start_button = tk.Button(
            button_frame,
            text= "START AUTOMATION",
            command=self.start_clicked,
            state="disabled",
            #cursor="hand2"
        )
        self.start_button.pack(side="left" ,padx=(0,15), ipadx=25, ipady=8)

        self.stop_button = tk.Button(
            button_frame,
            text="STOP AUTOMATION",
            command=self.stop_clicked,
            state="disabled",
            #cursor="hand2"
        )
        self.stop_button.pack(side="left", padx=(15,0),ipadx=25, ipady=8)

#!Status --------------------------------

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
            font=("Segoe UI", 9, "underline")
        )
        self.status_label.pack(anchor="w", pady=2)
#?--------------------
        self.current_part_label = ttk.Label(
            status_frame,
            text="Current Part : —"
        )
        self.current_part_label.pack(anchor="w", pady=2)
#?--------------------

        self.records_label = ttk.Label(
            status_frame,
            text="Records : 0/0"
        )
        self.current_part_label.pack(anchor="w", pady=2)

        # Small developer watermark
        ttk.Label(
            self,
            text="By Pranit Govande",
            font=("Segoe UI", 7),
            foreground="#717171"
        ).pack(
            side="bottom",
            pady=(0, 4)
            )

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

        self.file_label.config(text=f"{os.path.basename(file_path)}")

#? Update Status

        self.status_label.config(text=f"{len(parts)} Entries Loaded")
        self.current_part_label.config(text="Current Part : —")
        self.records_label.config(text=f"Records : 0 / {len(parts)}")

#? Reset Progress
        self.progress["maximum"] = len(parts)
        self.progress["value"] = 0
        self.progress_label.config( text=f"0 / {len(parts)}")

        self.start_button.config(state="normal", 
                    bg="#2E7D32",
                    fg="#FFFFFF",
                    disabledforeground="white",
                    activebackground="#256628",
                    activeforeground="white", 
                    cursor="hand2")


#!----------------------------------------
#! On CLICKING

    def start_clicked(self):

        self.stop_event.clear()
        
        if not self.parts:
            self.status_label.config(
            text="Status : Please select an Excel file."
        )
            return
        # try:
        #     delay = int(self.delay_spinbox.get())
        # except ValueError:
        #     self.status_label.config(
        #         text="Invalid Delay Value."
        #     )
        #     return

        # try:
        #     action_delay = float(self.action_delay_spinbox.get())
        # except ValueError:
        #     self.status_label.config(
        #         text="Status : Invalid Action Delay."
        #     )
        #     return
        # if not 0.05 <= action_delay <= 5.00:
        #     self.status_label.config( text= " Action Delay must be between 0.05 - 5.00 seconds.")
        #     return

        # Reset progress
        self.progress["value"] = 0
        self.progress_label.config(text=f"0 / {len(self.parts)}")
        self.records_label.config(text=f"Records : 0 / {len(self.parts)}")
        self.current_part_label.config(text="Current Part : —")

        # parts = read_part_numbers(self.selected_file)
        
        threading.Thread(
                target=run_automation,
                args=(
                    self.parts,
                    # delay,
                    # action_delay,
                    self.on_countdown,
                    self.on_progress,
                    self.on_complete,
                    self.on_stopped,
                    self.stop_event
                ),
                daemon=True
            ).start()
        

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal", 
            bg="#C62828",
            fg="white",
            activebackground="#A61F1F",
            activeforeground="white",
            cursor="hand2")

#! STATUS PROGRESS

    def on_countdown(self, seconds):

        self.after(
            0,
            lambda: self.status_label.config(text=f"Automation Begins in {seconds} seconds...")
        )

    def on_progress(self, current, total, part):

        def update():
            self.progress["maximum"] = total
            self.progress["value"] = current

            self. progress_label.config(text=f"{current} / {total}")
            self.records_label.config(text=f"Records : {current} / {total}")
            self.current_part_label.config(text=f"Current Part : {part}")
            self.status_label.config(text="Running...")

        self.after(0, update)

    def on_complete(self, total, part):

        def update():
            self.progress["maximum"] = total
            self.progress["value"] = total
            
            self. progress_label.config(text=f"{total} / {total}")
            self.records_label.config(text=f"Records : {total} / {total}")
            self.current_part_label.config(text=f"Last Processed Part : {part}")
            self.status_label.config(text=f"Completed. Processed {total} Records")

            self.start_button.config(state="normal", 
                        bg="#2E7D32",
                        fg="#FFFFFF",
                        disabledforeground="white",
                        activebackground="#256628",
                        activeforeground="white", cursor="hand2")
            self.stop_button.config(state="disabled", bg="SystemButtonFace", fg="SystemButtonText")

        self.after(0, update)

#! STOP BUTTON
    def stop_clicked(self):
        self.stop_event.set()

        self.stop_button.config(state="disabled", bg="SystemButtonFace",
    fg="SystemButtonText")

        self.status_label.config(text="Stopping Automation...")

    def on_stopped(self, processed):
        def update():

            self.status_label.config(text=f"Automation Stopped. Procesed {processed} Records.")
            self.current_part_label.config(text=f"Current Part : (Refer to Last ERP Entry if Present)")
            self.records_label.config(text=f"Records : {processed} / {len(self.parts)}")
            self.stop_button.config(state="disabled", bg="SystemButtonFace", fg="SystemButtonText")
            self.start_button.config(state="normal", bg="#2E7D32",
                        fg="#FFFFFF",
                        disabledforeground="white",
                        activebackground="#256628",
                        activeforeground="white", cursor="hand2")

        self.after(0, update)

