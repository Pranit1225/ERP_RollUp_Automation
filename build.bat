@echo off

echo ==========================================
echo   Macola Roll-Up Automation - Build
echo ==========================================
echo.

echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo.
echo Building executable...
pyinstaller --onefile --windowed --name "Macola Roll-Up Automation" --icon=assets\icon.ico src\main.py

echo.
echo ==========================================
echo   Build Complete
echo ==========================================
echo.
echo Executable:
echo dist\Macola Roll-Up Automation.exe
echo.

pause