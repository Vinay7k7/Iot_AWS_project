import json
import boto3

def lambda_handler(event, context):
    sns_topic_arn = 'arn:aws:sns:us-east-1:024085626319:Alert' # SNS topic ARN
    threshold = {
        'water_pressure': 65, # Replace with your water pressure threshold value
        'fire': 335, # Replace with your fire threshold value
        'air_pressure': 800 # Replace with your air pressure threshold value
    }

    # Connect to SNS
    sns_client = boto3.client('sns')
    
    # Accumulate high value messages
    high_value_messages = [f""]
    

    # Process incoming AWS IoT messages
    if 'Records' in event:
        payload = json.loads(event['Records'][0]['Sns']['Message'])
    else:
        payload = event
        
    
        

    # Extract water pressure, fire, and air pressure values
    water_pressure = payload.get('water_pressure',None)
    fire = payload.get('fire',None)
    air_pressure = payload.get('air_pressure',None)
    Block = payload.get('block',None)
    room = payload.get('room',None)
    floor = payload.get('floor',None)
    aka = f"There is a respective warnnings in {room} room in {floor} Floor {Block} Block at this time! \n So please kindly Don't panic Our rescuve Team is On his way Pleasse Stay safe \n In the Block:{Block} and the Room is:{room}"

    # Check if any value exceeds the threshold
    if water_pressure is not None and water_pressure > threshold['water_pressure']:
        message = f"Water pressure threshold exceeded: {water_pressure}"
        high_value_messages.append(message)

    if fire is not None and fire > threshold['fire']:
        message = f"Fire threshold exceeded: {fire}"
        high_value_messages.append(message)
        

    if air_pressure is not None and air_pressure > threshold['air_pressure']:
        message = f"Air pressure threshold exceeded: {air_pressure}"
        high_value_messages.append(message)
    high_value_messages.append(aka)
    # Publish high value messages to the SNS topic
    if high_value_messages:
        formatted_data = '\n'.join(high_value_messages)
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=formatted_data
        )
    return {
        'statusCode': 200,
        'body': 'Processing complete.'
    }
