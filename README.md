# AWS Cloud Data Handler Project

This Python script uses the AWS SDK (`boto3`) to manage AWS resources like EC2 instances, S3 buckets, and SQS queues. The script performs the following tasks:

1. Creates an EC2 instance, S3 bucket, and SQS queue.
2. Waits for 1 minute.
3. Lists all EC2 instances, S3 buckets, and SQS queues in AWS account.
4. Uploads a file to the S3 bucket.
5. Sends and retrieves a message from the SQS queue.
6. Deletes all the resources created.
7. Lists all resources after deletion to confirm.

## Prerequisites

- Python 3.x installed on your machine.
- The `boto3` library to interact with AWS services.
- Network access to AWS endpoints.


## Setup Instructions


### 1. Install Python

If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/). Ensure `pip` is installed as well for managing dependencies.

### 2. Install Dependencies

The script uses the `boto3` package to communicate with AWS services. Install the required dependencies using `pip`:

pip install boto3


### 3. Run the script 

Run the script using the following command:

python3 handler.py


### 4. Sample Output

Sample Terminal Output:

(venv) (base) Cloud Computing % python3 ./handler.py
Creating resources...
EC2 instance created with ID: i-0d66caf6e7a5fab9e
S3 bucket 'cse546testbucketunique' created
SQS queue 'CSE546testQueue.fifo' created with URL: https://sqs.us-west-2.amazonaws.com/381492105522/CSE546testQueue.fifo
Request sent, wait for 1 min...

Listing all resources...
EC2 Instance ID: i-0d66caf6e7a5fab9e
S3 Bucket Name: cse546testbucketunique
SQS Queue URL: https://sqs.us-west-2.amazonaws.com/381492105522/CSE546testQueue.fifo

Uploading file to S3 bucket...
File 'CSE546test.txt' uploaded to S3 bucket.

Sending message to SQS queue...
Message sent
Number of messages in SQS queue: 1

Pulling message from SQS queue...
Message Title: test message
Message Body: This is a test message
Message deleted from SQS queue.
Number of messages in SQS queue after pulling: 1

Waiting for 10 seconds...

Deleting resources...
S3 Bucket deleted
SQS queue 'CSE546testQueue.fifo' deleted
EC2 instance 'i-0d66caf6e7a5fab9e' terminated

Waiting for 20 seconds...

Listing all resources after deletion...
EC2 Instance ID: i-0d66caf6e7a5fab9e
SQS Queue URL: https://sqs.us-west-2.amazonaws.com/381492105522/CSE546testQueue.fifo

All actions completed.




