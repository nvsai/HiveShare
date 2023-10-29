#!/bin/sh

python3 --version
pip install pipenv
python3 -m venv  environment
. environment/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip install flask
pip install python-nmap
pip install tkinter
chmod +x run.sh
echo "please type './run.sh' and enter"

