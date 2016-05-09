import falcon
import sys
import json
import requests
from model.fact import Fact
import model.fact
from random import randint

class FactsController(object):
    def on_get(self, req, resp):
        facts = model.fact.read_facts()
        facts = json.loads(facts)
        number_of_facts = len(facts['facts'])
        index_random_fact = (randint(0,number_of_facts-1))
        fact = facts['facts'][index_random_fact]
        fact = Fact(fact_id=fact['id'], display=fact['display'])
        req.context['result'] = {"id": fact.get_fact_id(), "display": fact.get_display()}
        resp.status = falcon.HTTP_200
