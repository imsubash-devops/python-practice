import boto3
client = boto3.client("s3")
response = client.get_bucket_acl(
    Bucket='subash-demo-1816',
)
print(response)

"""response = client.create_bucket(
    Bucket='subash-demo-1816'

)
"""