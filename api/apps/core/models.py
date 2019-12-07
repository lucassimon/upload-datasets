# -*- coding: utf-8 -*-
# Python
from datetime import datetime

# Third
from mongoengine import StringField, DateTimeField, IntField

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

    dataset_id = StringField(required=True)
    row = IntField(required=True)
    column = StringField(required=True)
    message = StringField(required=True)
    value = StringField(required=True)

    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=get_today())
