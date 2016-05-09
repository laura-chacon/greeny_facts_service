import json
import boto
import os
from boto.s3.key import Key


s3 = boto.connect_s3(os.environ['ACCESS_KEY_ID'], 
                    os.environ['SECRET_ACCESS_KEY'])
facts_bucket = s3.get_bucket('greeny-facts')
k = Key(facts_bucket)

class Fact:
    def __init__(self, **kwargs):
        self.fact_id = kwargs.get("fact_id", None)
        self.display = kwargs.get("display", None)

    def get_fact_id(self):
        return self.fact_id

    def get_display(self):
        return self.display

def read_facts():
    k.key = 'facts.json'
    facts = k.get_contents_as_string()
    return facts
