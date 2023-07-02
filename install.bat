@echo off
if not exist venv (
    python -m venv venv
)
venv\Scripts\activate.bat
pip install -r requirements.txt
npm install


REM	Run this script first to install the python virtual environment and javascript packages 

REM	`install.sh` for Linux:
REM	#!/bin/bash
REM	if [ ! -d "venv" ]; then
REM	    python -m venv venv
REM	fi
REM	source venv/bin/activate
REM	pip install -r requirements.txt
REM	npm install
