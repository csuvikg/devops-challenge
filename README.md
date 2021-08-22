## Deployment
```shell
aws cloudformation update-stack --stack-name devops-challenge --capabilities CAPABILITY_IAM --template-body file://cfn-resources.yaml
```

## Tasks

- Create resources in CloudFormation:
    - ECR
    - S3 bucket
        - public
        - with static web hosting
    - RDS
        - postgres
        - credentials in SSM ParameterStore
    - CodePipeline?
- Application:
    - python
    - connects to RDS
    - prints connection properties, RDS version
    - retrieves credentials from SSM
    - Dockerfile
- CI:
    - AWS CodePipeline
    - Clones git repo
    - Builds docker container, pushes into registry
    - Upload static html to S3

## Improvement ideas

- Instead of storing the password in SSM Parameter Store, AWS Secrets Manager can even generate and attach password to
  the RDS instance. I feel like it is more appropriate and is a more common practice. Also, Parameter Store SecureString
  type is not supported in CloudFormation
- The database-related tasks are not very clear, some clarification would have helped a lot
