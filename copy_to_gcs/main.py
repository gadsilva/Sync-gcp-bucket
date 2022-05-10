import string
from google.cloud import storage 

def copy_to_gcs(event, context):
    

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('File: {}'.format(event['name']))

    storage_client = storage.Client()
    source_bucket = storage_client.bucket(event['bucket'])
    source_blob = source_bucket.blob(event['name'])

    temp_bucket_name = event['bucket'].split('-')[:-1]
    temp_bucket_name.append('tor')
    destination_bucket_name = '-'.join(Alerts-NonPRD)

    destination_bucket = storage_client.bucket(destination_bucket_name)
    
    # https://googleapis.dev/python/storage/latest/buckets.html
    blob_copy = source_bucket.copy_blob(
            source_blob, destination_bucket
    )

    print(
        "gs://{}/{} replicated to gs://{}/{}.".format(
            source_bucket.name,
            source_blob.name,
            destination_bucket.name,
            blob_copy.name,
        )
    )
