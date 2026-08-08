# Macola Roll-Up Automation

A lightweight Windows desktop automation tool that automates repetitive part-number entry into the Macola ERP Roll-Up process using data from an Excel workbook.

## Overview

During the Macola Roll-Up process, large Excel files containing hundreds or thousands of part numbers have to be entered into the ERP one record at a time.

The normal manual workflow requires the user to:

1. Select a part number from Excel.
2. Copy the value.
3. Paste it into the Macola ERP input field.
4. Press `Enter`.
5. Press `Enter` again for validation.
6. Repeat the process for every record.

This application automates that repetitive workflow.

The user only needs to select the Excel file, configure the start delay, and click inside the Macola ERP input field when instructed.

---

## Features

- Select `.xlsx` files through a Browse dialog
- Read part numbers from Column A
- Display the number of entries loaded
- Configurable automation start delay
- Countdown before automation begins
- Automated clipboard-based paste
- Automated `Enter` + `Enter` validation sequence
- Sequential processing of all records
- Live processing progress
- Current part number display
- Stop / Cancel automation
- Completion summary
- Start / Stop button state management
- No popup notifications during normal operation
- Standalone Windows `.exe` support

---

## Workflow

```text
Select Excel File
        ↓
Load Column A
        ↓
Display Entry Count
        ↓
Click START
        ↓
Countdown
        ↓
User focuses Macola ERP textbox
        ↓
Copy Part Number
        ↓
Paste into Macola
        ↓
Press Enter
        ↓
Press Enter
        ↓
Next Record
        ↓
Repeat Until End of File
        ↓
Display Completion Status
```

---

## Input Requirements

The Excel workbook must follow these requirements:

- File format: `.xlsx`
- Part numbers must be in **Column A**
- Records must be arranged continuously row by row
- No blank rows are expected within the data
- Each row represents one part number

Example:

| Column A   |
| ---------- |
| 124-1234-1 |
| 124-1234-2 |
| 124-1234-3 |
| 124-1234-4 |

---

## User Workflow

### 1. Launch the Application

Run:

```text
Macola Roll-Up Automation.exe
```

### 2. Select the Excel File

Click:

```text
Browse
```

and select the required `.xlsx` file.

The application displays the number of entries loaded.

### 3. Configure Start Delay

Set the required countdown duration in seconds.

The delay gives the user time to focus the Macola ERP input field.

### 4. Start Automation

Click:

```text
START AUTOMATION
```

During the countdown, click inside the Macola ERP part-number textbox.

### 5. Automation

The application sequentially processes every part number:

```text
Paste
Enter
Enter
```

and then moves to the next record.

### 6. Completion

When the final record has been processed, the application displays a completion status such as:

```text
Completed. Processed 1,034 Records.
```

---

## Stop Automation

The automation can be stopped using:

```text
STOP AUTOMATION
```

The application safely stops processing and displays the number of records processed before stopping.

The automation can subsequently be started again.

---

## Technology Stack

- **Python**
- **Tkinter** — Desktop GUI
- **OpenPyXL** — Excel file processing
- **PyAutoGUI** — Keyboard automation
- **Pyperclip** — Clipboard operations
- **PyInstaller** — Windows executable packaging

---

## Project Structure

```text
ERP_RollUp_Automation/
│
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── automation.py
│   └── excel_reader.py
│
├── assets/
│   └── icon.ico
│
├── sample_data/
│
├── tests/
│
├── docs/
│
├── requirements.txt
├── build.bat
├── README.md
├── LICENSE
└── .gitignore
```

---

## Development Setup

### Clone the Repository

```bash
git clone <repository-url>
cd ERP_RollUp_Automation
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running from Source

Run:

```bash
python src/main.py
```

---

## Building the Windows Executable

The project includes a build script:

```text
build.bat
```

Run it from the project root.

Alternatively:

```bash
pyinstaller --onefile --windowed --name "Macola Roll-Up Automation" src\main.py
```

The executable will be generated in:

```text
dist/
```

---

## Testing

The project includes a dedicated Test Cases & Test Execution Report covering:

- Application launch
- Excel file selection
- Excel data loading
- GUI control states
- Countdown
- Sequential automation
- Paste and validation sequence
- Progress tracking
- Completion
- Stop during countdown
- Stop during processing
- Automation restart
- Large-file processing

Testing was performed against the defined V1 functionality before release.

---

## Scope

### Included

- `.xlsx` input
- Column A processing
- Sequential part-number entry
- Macola keyboard automation
- Configurable start delay
- Progress tracking
- Stop functionality
- Completion reporting

### Currently Out of Scope

- Macola API integration
- Database integration
- Multiple Excel columns
- Multiple worksheets
- Automatic Macola navigation
- Advanced error recovery
- Automated invalid-part handling
- Scheduling
- OCR or image recognition
- Backend ERP integration

The application intentionally uses the existing Macola user interface and automates the established manual workflow.

---

## Version

**Current Version: v1.0.0**

Initial production release of the Macola Roll-Up Automation utility.

---

## License

This project is intended for internal organizational use.

---

**By Pranit Govande**
