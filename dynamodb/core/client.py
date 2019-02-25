import boto3

class AWSManager:
    def __init__(self):
        self.client = boto3.resource('dynamodb', region_name='us-east-1')