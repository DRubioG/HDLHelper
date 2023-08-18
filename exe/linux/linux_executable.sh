# bin/bash
rm -r ./main ./config ./icon.ico
cp -r ../../src/ ./

cd src
pyinstaller --onefile main.py --noconsole
cd dist
cp -r . ../../
cd ..
cp -r ./config/ ../
cd ..
cp ../../img/logo/icon.ico ./
rm -r ./src/