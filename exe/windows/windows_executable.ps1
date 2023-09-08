mkdir src
cd .\src\
Copy-Item "..\..\..\src\*"
pyinstaller.exe --onefile .\main.py
cd dist
Copy-Item ".\*" -Destination "..\..\..\"
cd ..
mkdir ..\config
Copy-Item ".\config\*" -Destination "..\config"
cd ..
#--Remove-Item 