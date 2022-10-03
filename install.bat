@echo off
set from=%cd%
set to=%UserProfile%\scripts

cd  %UserProfile%git
md scripts

echo Copy from %from%\spotdla.bat to %to%\spotdla.bat
copy %from%\spotdla.bat %to%\spotdla.bat

echo %UserProfile%\scripts add to the global path