import falcon
import falcon.testing as testing
import uuid
import main
import json
from model.fact import Fact
from types import UnicodeType
import model.fact
import six

class TestFactsController(testing.TestBase):
    def before(self):
        self.api = main.create_api()

    def test_success_get_fact(self):
        body = self.req()
        fact = json.loads(body)
        self.assertEqual(2, len(fact))
        self.assertTrue(type(fact['id']) is int)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)

    def req(self):
        headers = [('Accept', 'application/json'),
                       ('Content-Type', 'application/json'),]
        return self.simulate_request('/facts',
                                     headers=headers,
                                     decode='utf-8',
                                     method="GET",
                                     body="")
