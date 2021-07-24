#!/bin/bash
set -eo pipefail

# Create s3 bucket for aws resources
BUCKET_ID=$(dd if=/dev/random bs=8 count=1 2>/dev/null | od -An -tx1 | tr -d ' \t\n')
BUCKET_NAME=lambda-artifacts-$BUCKET_ID
echo $BUCKET_NAME > bucket-name.txt
aws s3 mb s3://$BUCKET_NAME

# Install python packages
rm -rf package
cd function
pip install --target ../package/python -r requirements.txt
cd ..

# Deploy using cloudformation
ARTIFACT_BUCKET=$(cat bucket-name.txt)
aws cloudformation package --template-file template.yml --s3-bucket $ARTIFACT_BUCKET --output-template-file out.yml
aws cloudformation deploy --template-file out.yml --stack-name aws-s3-lifecycle --capabilities CAPABILITY_NAMED_IAM
