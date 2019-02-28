from __future__ import print_function # Python 2/3 compatibility
from core.client import AWSManager
from core.generics import Generics

def app():
    print("""
        This program will perform below operations on dynamodb:
        - create table
        - add data to table
        - list the data from table
        - updated data from table
        - delete data from table
    """)
    client = AWSManager().client # boto3 dynamodb client reference
    dynamodb = Generics(client)
    dynamodb.create_table('users')
    newuser={
        'id': 1,
        'info': {
            'name':"Venkata Sai Katepalli",
            'email': "venkatasaikatepalli@gmail.com"
        }
    }
    dynamodb.add_to_table('users', newuser)

if __name__ == '__main__':
    app()