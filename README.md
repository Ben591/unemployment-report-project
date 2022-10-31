# unemployment-report-project

## Usage

```sh
python app/project_code.py
```

## Setup

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
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
python app/project_code.py

# of pass env var from command line:
ALPHAVANTAGE_API_KEY="_________" python app/project_code.py
```