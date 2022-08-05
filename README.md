# Flask Filereader
Simple Flask application that reads text file and return the content as response.

## Usage
By default, it reads file from `./files/replaceme.txt`. You can replace this by setting the environment variable `APP_FILE_PATH`

## Requirements
* Python 3.8.10

## Dev
Prepare Python environment
```sh
python -m venv .venv
source .venv/bin/activate
```

Install requirements
```sh
pip install pip --upgrade
pip install -r requirements.txt
```

Run
```sh
FLASK_APP=app.py flask run --host=0.0.0.0 --port=8000
```

Open app at [http://localhost:8000](http://localhost:8000)

## Docker
Docker hub link: [https://hub.docker.com/r/devsareno/flask-filereader](https://hub.docker.com/r/devsareno/flask-filereader)

Run
```sh
docker run --rm -p 8000:8000 devsareno/flask-filereader
```