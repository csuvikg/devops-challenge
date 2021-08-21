import boto3
from flask import Flask

app = Flask(__name__)

db_instance_name = ''

rds_client = boto3.client('rds')

dbs = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_name)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# - connects
# to
# RDS
# - prints
# connection
# properties, RDS
# version
# - retrieves
# credentials
# from SSM


# https://developer.okta.com/blog/2018/07/31/use-aws-cloudformation-to-automate-static-site-deployment-with-s3
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-package.html
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html
# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
