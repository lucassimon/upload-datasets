# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestDataset.test_should_response_dataset_paginated 1'] = {
    'data': [
        {
            'filename': 'Filename 0',
            'id': 'replaced to take snapshot',
            'path': '/path/to/uploaded',
            'status': 'initial'
        }
    ],
    'message': 'Dataset retornado(a).',
    'resource': 'Dataset',
    'status': 200
}
