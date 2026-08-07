import tkinter as tk
from tkinter import ttk

class RollupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Roll-Up Entry")
        self.root.geometry("650x450")

        self.enter_count = 0

        # ---------------- Input ----------------
        tk.Label(root, text="Paste Data:").pack(pady=(10, 2))

        self.entry = tk.Entry(root, width=70, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.focus()

        self.entry.bind("<Return>", self.handle_enter)

        # ---------------- Status ----------------
        self.status = tk.Label(root, text="", fg="green", font=("Arial", 11, "bold"))
        self.status.pack(pady=5)

        # ---------------- Table ----------------
        columns = ("No.", "Data")

        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)

        self.tree.heading("No.", text="No.")
        self.tree.heading("Data", text="Data")

        self.tree.column("No.", width=60, anchor="center")
        self.tree.column("Data", width=550)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.counter = 1

    def handle_enter(self, event):
        text = self.entry.get().strip()

        if text == "":
            return "break"

        self.enter_count += 1

        if self.enter_count == 1:
            self.status.config(text="Press Enter again to Confirm", fg="orange")

        elif self.enter_count == 2:
            self.tree.insert(
                "",
                "end",
                values=(self.counter, text)
            )

            self.counter += 1

            self.status.config(text="✔ Success!", fg="green")

            self.entry.delete(0, tk.END)
            self.entry.focus()

            self.enter_count = 0

        return "break"


root = tk.Tk()
app = RollupGUI(root)
root.mainloop()