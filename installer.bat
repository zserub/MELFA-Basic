@echo off
:: Check if python installed
@REM python --version >nul 2>&1
@REM if %errorlevel% neq 0 (
@REM     echo Python is not installed.
@REM     echo Please install Python and try again.
@REM ) else (
@REM     echo Python is installed.
@REM )

:: Put formatter script to the root folder
copy "formatter\formatter.exe" "..\..\..\..\"
if %errorlevel% neq 0 (
    echo Error: Failed to copy the file.
) else (
    echo File copied successfully.
)
pause