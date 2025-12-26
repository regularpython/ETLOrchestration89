
from dotenv import load_dotenv
import os
import json
load_dotenv()

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError
def get_secret():

    secret_name = "dev/app/mysql"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = json.loads(get_secret_value_response['SecretString'])

    return secret
    # Your code goes here.



ENV = os.getenv("environment")

if ENV == "Dev":
    result = get_secret()
    rds_access_protocol = result['RDS_ACCESS_PROTOCOL']
    rds_username = result['RDS_USERNAME']

elif ENV == "local":

    rds_access_protocol = os.getenv("RDS_ACCESS_PROTOCOL")
    rds_username = os.getenv("RDS_USERNAME")
    rds_password = os.getenv("RDS_PASSWORD")
    rds_host = os.getenv("RDS_HOST")
    rds_port = os.getenv("RDS_PORT")
    rds_db_name = os.getenv("RDS_DB_NAME")

elif ENV == "Test":
    rds_access_protocol = os.getenv("RDS_ACCESS_PROTOCOL")

else:
    raise Exception()

print(rds_access_protocol)
    # print(rds_username)