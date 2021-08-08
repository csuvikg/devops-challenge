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