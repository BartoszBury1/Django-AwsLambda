import csv
import json
import boto3
import pandas as pd
import os
import glob


s3 = boto3.resource("s3", aws_access_key_id="777", aws_secret_access_key="778", endpoint_url="http://s3.localhost.localstack.cloud:4566")
s = boto3.client("s3", endpoint_url="http://s3.localhost.localstack.cloud:4566/", region_name='us-east-1')

bucket_name = 'my-bucket'


s.create_bucket(Bucket=bucket_name)


files = os.path.join("Csv/example*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_json('CombFile.json')


with open ("CombFile.json", "w") as f:
    s3object = s3.Object(bucket_name, "CombFile.json")

    s3object.put(Body=(bytes(json.dumps("CombFile.json").encode("UTF-8"))))