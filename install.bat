@echo off
title ASCII Art Generator - Installation
color 0A

echo.
echo =========================================
echo    ASCII ART GENERATOR - INSTALLATION
echo =========================================
echo.

cd /d "%~dp0"

echo [+] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [-] ERROR: Python not installed
    echo [!] Download from: https://python.org
    pause
    exit /b 1
)

echo [+] Python detected successfully!
echo.

echo [+] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo [-] ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [+] Installation completed successfully!
echo [+] Launch with: python main.py
echo.
pause
