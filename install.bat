@echo off
set from=%cd%
set to=%UserProfile%\scripts

cd  %UserProfile%
md scripts

echo Copy from %from%\spotdla.bat to %to%\spotdla.bat
copy %from%\spotdla.bat %to%\spotdla.bat
echo Copy from %from%\spotdla.py to %to%\spotdla.py
copy %from%\spotdla.py %to%\spotdla.py

echo %UserProfile%\scripts add to the global path