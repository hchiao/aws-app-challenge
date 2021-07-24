# AWS SDK Application

Write an application that uses the AWS SDK to manage the lifecycle of an AWS resource including creation, update, and deletion.

It is intended that anyone should be able to clone the repository and run locally by providing valid AWS credentials, or packaged and run remotely if the end user desires (including packaging and CI for remote execution is not required, but the app should be written with a production mindset).

Include documentation on build/run process and minimal other documentation wherever necessary/helpful.
Optionally, include CI and/or build automation config.

The quality of your code is being evaluated.

Free choice of:
- Lifecycle eventing
- Language
- AWS resource/s

## Lifecycle Eventing

Events/triggers for moving through lifecycle phases are up to you. Your application can progress through lifecycle phases by configuration, api calls, time, or any other method you feel appropriate.

The application should manage at least three lifecycle stages - create, update (configuration change), and delete.

## Language

Feel free to use whichever programming language you are most comfortable with or is best suited.

## AWS Resource/s

You may manage an EC2 instance, S3 bucket, route53 zone, dynamodb table, or any other resource you feel allows you to demonstrate lifecycle management.
