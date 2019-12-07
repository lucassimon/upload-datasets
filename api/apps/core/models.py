# -*- coding: utf-8 -*-
# Python
from datetime import datetime

# Third
from mongoengine import StringField, DateTimeField

# Apps
from apps.db import db
from apps.utils import get_today

from .choices import STATUS, INITIAL


class Dataset(db.Document):
    meta = {"collection": "datasets"}

    filename = StringField(required=True)
    path = StringField(required=True)
    status = StringField(required=True, choices=STATUS, default=INITIAL)

    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=get_today())


class Log(db.Document):
    meta = {"collection": "logs"}

    # '{row: 0, column: "status"}: "unavailable" is not in the list of legal options (pending, paid, due, error)'

    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=get_today())
