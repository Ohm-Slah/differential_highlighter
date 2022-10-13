@echo off
echo checking Python install...

:: Check for Python Installation
py --version 3>NUL
if errorlevel 1 goto errorNoPython

:: Reaching here means Python is installed.

echo Installing required packages...

pip3 install termcolor

py differential_highlighter.py

pause

:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python 3+ not installed
pause