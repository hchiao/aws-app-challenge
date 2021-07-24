import os
import logging
import jsonpickle
import boto3
import json
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

client = boto3.client('lambda')
client.get_account_settings()

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('-----------------------------')
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('-----------------------------')
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    operation = event['path']

    client = boto3.client('dynamodb', region_name=os.environ["AWS_DEFAULT_REGION"])

    operations = {
        '/dbcreate': lambda x: client.create_table(**x),
        '/dbput': lambda x: client.update_table(**x),
        '/dbdelete': lambda x: client.delete_table(**x),
    }

    logger.info(json.loads(event['body']))

    try:
        if operation in operations:
           res = operations[operation](json.loads(event['body']))
           logger.info(res)
           return {
               'statusCode': 200,
               'body': json.dumps('Success')
           }
        else:
            raise ValueError('Unrecognized operation "{}"'.format(operation))
    except:
        return {
            'statusCode': 500,
            'body': json.dumps('Error')
        }
