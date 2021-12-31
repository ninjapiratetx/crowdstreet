To run this
install python vestion 3.10:
https://www.python.org/downloads/

install pip and virtualenv:
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv

Create virtual environment:
python3 -m venv .venv

Start virtual environment:
source .venv/bin/active

Install the requirements:
pip3 install -r requirements.txt

cd into tests:
cd tests

run pytest which will start a browser and run the tests:
pytest
