import string
from google.cloud import storage 

def copy_to_gcs(event, context):
    

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('File: {}'.format(event['name']))

    storage_client = storage.Client()
    source_bucket = storage_client.bucket(event['exyon_bucket'])
    source_blob = source_bucket.blob(event['name'])

    # split on '-' and drop location identifier ('mtl')
    temp_bucket_name = event['bucket'].split('-')[:-1]
    # add 'tor' to the list and rejoin on '-'
    temp_bucket_name.append('exyon_bucket_prod')
    destination_bucket_name = '-'.join(temp_bucket_name)

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