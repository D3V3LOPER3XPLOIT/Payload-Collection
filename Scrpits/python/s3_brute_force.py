import boto3
import botocore
import time

s3 = boto3.client('s3')

with open("bucketlist.txt") as f:
    for bucket in f:
        bucket = bucket.strip()
        try:
            s3.head_bucket(Bucket=bucket)
            print(f"[✓] FOUND PUBLIC or AUTHENTICATED ACCESS: {bucket}")
        except botocore.exceptions.ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 403:
                print(f"[!] ACCESS DENIED (403): {bucket}")
            elif error_code == 404:
                print(f"[✗] NOT FOUND (404): {bucket}")
            else:
                print(f"[?] UNKNOWN ERROR for {bucket}: {e}")
        time.sleep(0.5)  # optional: avoid rate-limiting
