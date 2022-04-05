@echo off
echo Installing required packages...

:: Check for Python Installation
python3 --version 3>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.

pip3 install termcolor

python3 differential_highlighter.py

pause

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python 3+ not installed
pause