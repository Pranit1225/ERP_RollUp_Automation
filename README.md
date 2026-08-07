# Macola Roll-Up Automation

Desktop automation utility for automating Roll-Up data entry into Macola ERP.

## Features

- Read Excel (.xlsx)
- Process Column A
- Paste into ERP
- Press Enter twice
- Configurable start delay
- Success summary

## Tech Stack

- Python
- Tkinter
- OpenPyXL
- PyAutoGUI
- Pyperclip

## Build

```bash
pyinstaller --onefile --windowed src/main.py
```
