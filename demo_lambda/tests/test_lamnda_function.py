from unittest import TestCase
from demo_lambda.lambda_function import lambda_handler, create_elasticsearch_index
from elasticsearch import Elasticsearch
from unittest.mock import patch


class LambdaTests(TestCase):

    @patch.object(Elasticsearch, 'index', return_value={'result': 'index created'})
    def test_create_elastic_search_index(self, mock_elk_response):
        result = create_elasticsearch_index(author='foo', text='bar')
        self.assertEqual(result, 'index created')


    def test_lambda_handler(self):
        result = lambda_handler(event="", context="")
        self.assertEqual(result, "Hello Lambda")