from dataclasses import dataclass
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor
import csv
from os import getenv



host = "apps-database.ccr79owffman.us-east-1.rds.amazonaws.com"
username = "postgres"
password = "dafnyx1234"
database ="postgres"

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = getenv('password')
)

def lambda_handler(event, context):
    cur = conn.cursor()

    s3 = boto3.resource('s3')
    bucket_name = 'my-new-bucket-asdiaonsdnioadsnoi'
    key = 'my_data.csv'
    s3.Bucket(bucket_name).download_file(key, '/tmp/my_data.csv')
    

    with open('/tmp/my_data.csv', newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            
            try:
                rating = float(row[3])
                rating_count = int(row[4])
                maximum_installs = int(row[5])
            except Exception as e:
                continue
            
            cur.execute("INSERT INTO apps_schema.playstore(app_name, app_id, category, rating, rating_count, maximum_installs, last_updated, content_rating, ad_supported, market_segment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],rating,rating_count,maximum_installs,row[6],row[7],row[8],row[9]))
    conn.commit()
    cur.close()
    conn.close()

