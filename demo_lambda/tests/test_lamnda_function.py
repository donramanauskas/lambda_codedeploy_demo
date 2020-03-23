from unittest import TestCase
from demo_lambda.lambda_function import lambda_handler


class LambdaTests(TestCase):

    def test_lambda_handler(self):
        result = lambda_handler(event="", context="")
        self.assertEquals(result, "Hello Lambda")