from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

def create_elasticsearch_index(author, text):
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", id=1, body=doc)
    print(res['result'])


def lambda_handler(event, context):
    return "Hello Lambda"