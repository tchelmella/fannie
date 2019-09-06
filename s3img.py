import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SCRET_KEY = ''
BUCKET_NAME = 'tulsidas'

data = open('Andrews_curves.png','rb')

s3 = boto3.resource(
	's3',
	aws_access_key_id=ACCESS_KEY_ID,
	aws_secret_access_key=ACCESS_SECRET_KEY,
	config=Config(signatre_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='Andrews_curves.png',Body=data)

print("Done")
