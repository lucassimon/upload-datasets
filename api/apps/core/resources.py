import os
import uuid
from flask import request, current_app
from flask.wrappers import Response as FlaskResponse


# Third

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from mongoengine.errors import NotUniqueError, ValidationError

# Apps
from apps.messages import Messages
from apps.responses import Response


# Local
from . import repositories, models, tasks


class DatasetUploadResource(Resource):
    def post(self, *args, **kwargs):
        resource = "Dataset upload"
        response = Response(resource)
        repo = repositories.DatasetRepo()

        parse = reqparse.RequestParser()
        parse.add_argument("dataset_file", type=FileStorage, location="files")
        parse.add_argument("kind", type=str, location="form")
        args = parse.parse_args()

        file = args["dataset_file"]
        kind = args["kind"]

        if file:
            extension = os.path.splitext(file.filename)[1]
            filename = str(uuid.uuid4()) + extension

            # TODO: Improve it to save the file on s3 bucket
            # TODO: The file is too large to upload, so the best choice is:
            # TODO: - save the zipped file
            # TODO: - put the file directly on s3 from FRONT END

            path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            try:
                payload = {
                    "filename": filename,
                    "path": current_app.config["UPLOAD_FOLDER"],
                }
                dataset = repo.create(payload)

                # TODO: If the upload was did directly to s3 we can send the create event
                # to rabbitmq or sqs to process this file uploaded instead use celery
                tasks.process(f"{dataset.id}", kind)

            except (NotUniqueError, ValidationError, Exception) as e:
                response.exception(description=e.__str__())

            return response.ok(
                Messages.RESOURCE_CREATED.value.format(resource), data={}
            )

        return response.data_invalid(
            {"file": "Não encontramos um arquivo a ser carregado"}
        )
