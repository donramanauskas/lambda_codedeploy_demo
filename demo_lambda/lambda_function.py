import boto3
from elasticsearch import Elasticsearch

client = boto3.client('ecr')


def lambda_handler(event, context):
    response = client.describe_repositories()['repositories'][0]['repositoryName']
    print(response)