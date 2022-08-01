pip3 install virtualenv;
python3 -m venv venv;
. venv/bin/activate;
pip3 install -r requirements.txt;
pre-commit install;
docker-compose up;
