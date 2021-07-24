#!/bin/bash
set -eo pipefail
STACK=aws-s3-lifecycle
FUNCTION=$(aws cloudformation describe-stack-resource --stack-name $STACK --logical-resource-id function --query 'StackResourceDetail.PhysicalResourceId' --output text)
aws cloudformation delete-stack --stack-name $STACK
rm -f out.yml out.json function/*.pyc
rm -rf package function/__pycache__
ARTIFACT_BUCKET=$(cat bucket-name.txt)
aws s3 rb --force s3://$ARTIFACT_BUCKET
rm bucket-name.txt
aws logs delete-log-group --log-group-name /aws/lambda/$FUNCTION;