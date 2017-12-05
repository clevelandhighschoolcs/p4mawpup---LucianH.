@echo off
set myvar=%cd%
:choice
set /P  input=Do you want to make the folder in the current directory? "%myvar%" (Y/N)
If /I "%input%"=="y" goto yes 
If /I "%input%"=="n" goto no
goto :choice

:yes
set myvar=%cd%
set /p FolderName=Folder name (no spaces):
mkdir %FolderName%
cd %myvar%\%FolderName%
c:\Python27\Scripts\virtualenv -p c:\Python27\python.exe .lpvenv
.lpvenv\Scripts\activate
@echo on

:no
set /p dirname=%cd%\
cd %cd%\%dirname%
goto :yes



