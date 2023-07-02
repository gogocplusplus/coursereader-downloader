@echo off
:loop
node pdfmaker.js
goto loop

REM	Lines below are comments
REM	Run this script after install.bat is completed
REM	This bat script uses node.js to run pdfmaker.js in a loop
REM	Pdfmaker.js will exec the pdfcombiner.py every time it runs
REM	The line `call ./venv/scripts/activate && python pdfcombiner.py`
REM	automatically activates the virtual environment .venv
REM	and then runs the virtual environment's local and not global python.exe

REM	If you're on linux then the below is a sample `run.sh` script you would create - remove REM and tabs
REM	#!/bin/bash
REM	while true
REM	do
REM 		node pdfmaker.js
REM	done