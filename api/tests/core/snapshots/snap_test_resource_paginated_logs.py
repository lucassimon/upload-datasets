# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestLog.test_should_response_logs 1'] = {
    'data': [
        {
            'id': 'replaced to take snapshot'
        },
        {
            'id': 'replaced to take snapshot'
        },
        {
            'id': 'replaced to take snapshot'
        },
        {
            'id': 'replaced to take snapshot'
        }
    ],
    'message': 'Lista os/as Logs from dataset paginados(as).',
    'page': 1,
    'pages': 1,
    'params': {
        'page_size': 10
    },
    'resource': 'Logs from dataset',
    'status': 200,
    'total': 4
}
