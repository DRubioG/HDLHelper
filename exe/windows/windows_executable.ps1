mkdir src
cd .\src\
Copy-Item "..\..\..\src\*"
python -m PyInstaller --onefile .\main.py
cd dist
Copy-Item ".\*" -Destination "..\..\"
cd ..
mkdir ..\config
Copy-Item ".\config\*" -Destination "..\config"
cd ..
Remove-Item .\src\ -Recurse