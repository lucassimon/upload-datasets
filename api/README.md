# API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Redis `docker run -d --name redis -p 6379:6379 -i -t redis:3.2.5-alpine`

- Python 3.6+

You should use virtual environments when developing Python applications. Check [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

### Installing

First, clone the repository, then run

If you are using virtual environments (strongly recommended, since your project dependencies and variables aren't shared with each other when you use them), run:

```
workon <your-virtual-environment> 
python3 -m venv .venv
```

To install project dependencies, run

```
pip install -r requirements/dev.txt
```

## Testing
```
make coverage or make test or pytest
```

## Running

```
flask run or make run or python application.py
```

This will start the application on http://localhost:5000.

## Celery

`celery worker -A celery_worker.celery --loglevel=info --pool=solo`
