from apps.celery import celery

# from celery import shared_task


@celery.task()
def unzip_file(object_id):
    print("ola")
