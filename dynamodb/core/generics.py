import json

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

class Generics(object):
    def __init__(self, client):
        self.client = client
    
    def create_table(self, table_name):
        table = self.client.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  #Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'email',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        print("Table status:", table.table_status)
    
    def add_to_table(self, table_name, data):
        table = self.client.Table(table_name)
        response = table_name.put_item(Item=data)
        print("PutItem succeeded:")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))