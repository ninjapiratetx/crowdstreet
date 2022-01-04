# crowdstreet

# To run this
## install python vestion 3.10:
https://www.python.org/downloads/

## install pip and virtualenv:
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv

## Install chromedriver
https://www.swtestacademy.com/install-chrome-driver-on-mac/

## Create virtual environment:
python3 -m venv .venv

## Start virtual environment:
source .venv/bin/active

## Install the requirements:
pip3 install -r requirements.txt

## run pytest which will start a browser and run the tests:
cd into tests:
cd tests
export PASSWORD=<your passowrd>
export PYTHONPATH=$PYTHONPATH:$HOME/crowdstreet
export PATH=$PATH:<PATH TO where chromedriver is>
pytest

# Future work
bug - move the refresh to defaults to press Captacha
bug - making the test flakey.  need to add a check to it's cliked.  while  not click agaign
Get find capatch to work - You may have to frame it still
