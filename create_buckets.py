#Creating the Connection
import boto3

s3 = boto3.resource('s3')

#Creating a Bucket

s3.create_bucket(Bucket='ta-test-boto3-python-labs')

s3.create_bucket(Bucket='ta-test-boto3-python-labs', CreateBucketConfiguration={
    'LocationConstraint': 'eu-central-1'})

#Storing Data

s3.Object('ta-test-boto3-python-labs', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))
