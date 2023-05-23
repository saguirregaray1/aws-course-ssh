import boto3
import datetime
import json

def lambda_handler(event, context):
    # Specify the RDS instance identifier
    rds_instance_id = 'apps-database'

    # Create a RDS client
    rds_client = boto3.client('rds')

    # Stop the RDS instance
    response = rds_client.stop_db_instance(DBInstanceIdentifier=rds_instance_id)

    # Convert datetime object to string representation
    response['StopTime'] = response['StopTime'].isoformat()

    # Return the response as JSON
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
