import boto3
import time
import os

# Load AWS credentials from environment variables or IAM role
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region = 'us-west-2'

# Create a session object using AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)

# Initialize clients for EC2, S3, and SQS services
ec2_client = session.client('ec2')
s3_client = session.client('s3', region_name=region)
sqs_client = session.client('sqs')

# Step 3: Create resources
print("Creating resources...")

# Create EC2 instance
ec2_response = ec2_client.run_instances(
    ImageId='ami-05134c8ef96964280',
    KeyName='Key_Pair_Name',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
instance_id = ec2_response['Instances'][0]['InstanceId']
print(f"EC2 instance created with ID: {instance_id}")

# Create S3 bucket
bucket_name = 'cse546testbucketunique'
s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
print(f"S3 bucket '{bucket_name}' created")

# Create SQS queue
queue_name = 'CSE546testQueue.fifo'
sqs_response = sqs_client.create_queue(QueueName=queue_name, Attributes={
    'FifoQueue': 'true'
})
queue_url = sqs_response['QueueUrl']
print(f"SQS queue '{queue_name}' created with URL: {queue_url}")

# Wait for 1 minute
print("Request sent, wait for 1 min...")
time.sleep(60)

# Step 5: List all resources
print("\nListing all resources...")

# List EC2 instances
ec2_instances = ec2_client.describe_instances()
for reservation in ec2_instances['Reservations']:
    for instance in reservation['Instances']:
        print(f"EC2 Instance ID: {instance['InstanceId']}")

# List S3 buckets
buckets = s3_client.list_buckets()
for bucket in buckets['Buckets']:
    print(f"S3 Bucket Name: {bucket['Name']}")

# List SQS queues
queues = sqs_client.list_queues()
for queue in queues.get('QueueUrls', []):
    print(f"SQS Queue URL: {queue}")

# Step 6: Upload a file to S3 bucket
print("\nUploading file to S3 bucket...")
s3_client.put_object(Bucket=bucket_name, Key='CSE546test.txt', Body='')
print("File 'CSE546test.txt' uploaded to S3 bucket.")

# Step 7: Send a message to SQS queue
print("\nSending message to SQS queue...")
sqs_client.send_message(
    QueueUrl=queue_url,
    MessageBody='This is a test message',
    MessageGroupId='CSE546Group',
    MessageDeduplicationId='test12345',
    MessageAttributes={
        'Title': {
            'StringValue': 'test message',
            'DataType': 'String'
        }
    }
)

print("Message sent")

# Step 8: Check messages in SQS queue
messages = sqs_client.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])
print(f"Number of messages in SQS queue: {messages['Attributes']['ApproximateNumberOfMessages']}")
