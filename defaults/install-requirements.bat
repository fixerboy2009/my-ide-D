@echo off

echo Upgrading PIP before installing requirements....
pip install --upgrade pip

echo Installing colorama (1 of 2)
pip3 install colorama

echo Installing playsound (2 of 2)
pip3 install playsound

echo Installed!