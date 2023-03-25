# bin/bash
rm -r ./main ./config
cp -r ../../src/ ./
cd src
pyinstaller --onefile main.py
cd dist
cp -r . ../../
cd ..
cp -r ./config/ ../
cd ..
rm -r ./src/