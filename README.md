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