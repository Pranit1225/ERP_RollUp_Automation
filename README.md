# Macola Roll-Up Automation

A lightweight Windows desktop automation tool that automates repetitive part-number entry into the Macola ERP Roll-Up process using data from an Excel workbook.

## Overview

During the Macola Roll-Up process, large Excel files containing hundreds or thousands of part numbers have to be entered into the ERP one record at a time.

The normal manual workflow requires the user to:

1. Select a part number from Excel.
2. Copy the value.
3. Paste it into the Macola ERP input field.
4. Press `Enter`.
5. Wait for ERP validation.
6. Press `Enter` again to confirm.
7. Repeat the process for every record.

This application automates that repetitive workflow.

The user only needs to select the Excel file, configure the start delay and validation delay, and click inside the Macola ERP input field when instructed.

---

## Features

- Select `.xlsx` files through a Browse dialog
- Read part numbers from Column A
- Display the number of entries loaded
- Configurable automation start delay
- Configurable validation delay
- Countdown before automation begins
- Automated clipboard-based paste
- Automated `Enter` + configurable delay + `Enter` validation sequence
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
Configure Start Delay
        ↓
Configure Validation Delay
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
Validation Delay
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

The start delay gives the user time to focus the Macola ERP input field before automation begins.

### 4. Configure Validation Delay

Set the required validation delay.

The validation delay controls the time between the first and second `Enter` presses during ERP validation.

The available values are:

```text
0.1
0.5
1.0
1.5
2.0
```

Use a higher value when additional processing time is required by the Macola ERP/server.

### 5. Start Automation

Click:

```text
START AUTOMATION
```

During the countdown, click inside the Macola ERP part-number textbox.

### 6. Automation

The application sequentially processes every part number:

```text
Paste
Enter
Validation Delay
Enter
```

and then moves to the next record.

### 7. Completion

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
pyinstaller --onefile --windowed --name "Macola Roll-Up Automation" --icon=assets\icon.ico src\main.py
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
- Start countdown
- Validation delay
- Sequential automation
- Paste and validation sequence
- Progress tracking
- Completion
- Stop during countdown
- Stop during processing
- Automation restart
- Large-file processing

The application was tested with the Macola ERP environment and the automation workflow was successfully verified.

---

## Scope

### Included

- `.xlsx` input
- Column A processing
- Sequential part-number entry
- Macola keyboard automation
- Configurable start delay
- Configurable validation delay
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

**Current Version: v1.1.0**

### v1.1.0

Added configurable Validation Delay between the first and second `Enter` presses during ERP validation.

The configurable delay allows the user to adjust the automation speed according to the processing response of the Macola ERP/server.

---

## License

This project is intended for internal organizational use.

---

**By Pranit Govande**
