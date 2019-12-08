# -*- coding: utf-8 -*-

# Third
from flask_restful import Api, Resource

# Apps
from apps.messages import Messages
from apps.core import resources as CoreResources


_API_ERRORS = {
    "UserAlreadyExistsError": {"status": 409, "message": Messages.ALREADY_EXISTS.value},
    "ResourceDoesNotExist": {
        "status": 410,
        "message": Messages.RESOURCE_DOES_NOT_EXIST.value,
    },
    "MethodNotAllowed": {"status": 405, "message": Messages.RESOURCE_NOT_ALLOWED.value},
    "NotFound": {"status": 404, "message": Messages.RESOURCE_NOT_FOUND.value},
    "BadRequest": {"status": 400, "message": Messages.RESOURCE_BAD_REQUEST.value},
    "InternalServerError": {
        "status": 500,
        "message": Messages.RESOURCE_BAD_REQUEST.value,
    },
}


class Index(Resource):
    def get(self):
        return {"hello": "world by apps"}


api = Api(errors=_API_ERRORS)


def configure_api(app):

    api.add_resource(Index, "/")

    api.add_resource(CoreResources.DatasetUploadResource, "/upload")

    api.add_resource(CoreResources.DatasetPageList, "/datasets/page/<int:page_id>")
    api.add_resource(CoreResources.DatasetResource, "/datasets/<string:dataset_id>")

    api.add_resource(
        CoreResources.LogsPageList, "/logs/<string:dataset_id>/page/<int:page_id>"
    )

    api.init_app(app)
