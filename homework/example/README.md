# Example

This is a simple hello-world python script. 

## Setup

Follow these instructions:

1. Create a python virtual environment.
    * Ex: `python3 -m virtualenv --python=python3 venv`
1. Activate the virtualenv.
    * MacOS / Linux: `source venv/bin/activate`
    * Windows: `source venv/Scripts/activate`
1. Install requirements:
    * `pip install -r requirements.txt`

## Usage

You can run the script with the following command:

```commandline
$ python main.py
```

```commandline
$ APP_LOG_LEVEL="WARN" python main.py
```

Check the code style with:

```commandline
$ pycodestyle . --exclude venv
```
