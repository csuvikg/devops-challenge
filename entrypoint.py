from os import environ

import boto3

ssm_client = boto3.client('ssm')
db_password = ssm_client.get_parameter(Name=environ['SSM_PARAMETER_NAME'])['Parameter']['Value']

rds_client = boto3.client('rds')
dbs = rds_client.describe_db_instances(DBInstanceIdentifier=environ['DB_INSTANCE_NAME'])['DBInstances']

for db in dbs:
    print('** RDS Version **')
    print(f"Engine: {db['Engine']} (v{db['EngineVersion']})")

    print('\n** Connection details **')
    print(f"Host: {db['Endpoint']['Address']}")
    print(f"Port: {db['Endpoint']['Port']}")
    print(f"User: {db['MasterUsername']}")
    print(f"Password: {db_password}")
