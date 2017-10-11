@ECHO off
selocal EnableDelayedExpansion

ECHO START RUN CASES
%~d0  
cd %~dp0  
start pythonw testSet\run.py
ECHO END RUN
PAUSE 