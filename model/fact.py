import json
import boto
import os
from boto.s3.key import Key
import boto3

client = boto3.client(
    's3',
    region_name='eu-west-1',
    aws_access_key_id=os.environ['ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['SECRET_ACCESS_KEY']
)

class Fact:
    def __init__(self, **kwargs):
        self.fact_id = kwargs.get("fact_id", None)
        self.display = kwargs.get("display", None)

    def get_fact_id(self):
        return self.fact_id

    def get_display(self):
        return self.display

def read_facts():
    response = client.get_object(
        Bucket='greeny-facts',
        Key='facts.json'
    )
    return response['Body'].read()
