#!/bin/bash
set -eo pipefail

# Create s3 bucket for aws resources
BUCKET_ID=$(dd if=/dev/random bs=8 count=1 2>/dev/null | od -An -tx1 | tr -d ' \t\n')
BUCKET_NAME=lambda-artifacts-$BUCKET_ID
echo $BUCKET_NAME > bucket-name.txt
aws s3 mb s3://$BUCKET_NAME

# Deploy using cloudformation
ARTIFACT_BUCKET=$(cat bucket-name.txt)
aws cloudformation package --template-file template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file output.yml
aws cloudformation deploy --template-file output.yml --stack-name aws-s3-lifecycle --capabilities CAPABILITY_NAMED_IAM
