# -*- coding: utf-8 -*-

# Python
from os.path import dirname, isfile, join

import pytest
from dotenv import load_dotenv

_ENV_FILE = join(dirname(__file__), "../.env")

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


@pytest.fixture(scope="session")
def client():
    from apps import create_app

    flask_app = create_app("testing")

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope="session")
def auth(client):
    # TODO: Put auth User and tokens here
    return client


@pytest.fixture(scope="session")
def mongo(request, auth):
    from apps.db import db

    yield db

    def fin(db):
        print("\n[teardown] disconnect from db")

    db.connection.drop_database("dataset_test")
    db.connection.close()
    fin(db)
