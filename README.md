# unemployment-report-project

## Usage

```sh
python app/project.py
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```

Run the unemployment report:

```sh
python app/project.py

# of pass env var from command line:
ALPHAVANTAGE_API_KEY="_________" python app/project.py
```

## Testing

Run tests:

```sh
pytest
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```