# Third
from marshmallow import Schema
from marshmallow.fields import Str, Date

# Apps
from apps.messages import Messages


class CommonDataSet(Schema):
    id = Str(required=True)
    filename = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    path = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )
    status = Str(
        required=True, error_messages={"required": Messages.FIELD_REQUIRED.value}
    )


class ListDataSetSchema(CommonDataSet):
    pass


class DetailDataSetSchema(CommonDataSet):
    pass


class ListLogSchema(Schema):
    id = Str(required=True)
    dataset_id = Str(required=True)
    row = Str(required=True)
    column = Str(required=True)
    message = Str(required=True)
    value = Str(required=True)
