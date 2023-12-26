import boto3

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'FormMessages'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Define the query condition
partition_key_value = '20231101'
sort_key_prefix = ''

# Query the table
response = table.query(
     KeyConditionExpression='submitDate = :partition_key_value',
     ExpressionAttributeValues={
        ':partition_key_value': partition_key_value
    }
)

# Retrieve the queried items
items = response['Items']

# Print the queried items

for item in items:
    print(item)


'''
import boto3

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Specify the table name and index name
table_name = 'Form'
index_name = 'AttributeIndex'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Define the query condition
partition_key_value = '2023'
sort_key_prefix = '2023'

# Query the table using the index
response = table.query(
    IndexName=index_name,
    KeyConditionExpression='submitdate = :partition_key_value AND begins_with(submitTime, :sort_key_prefix)',
    ProjectionExpression='attribute_name',  # Specify the attribute to include in the result
    ExpressionAttributeValues={
        ':partition_key_value': partition_key_value,
        ':sort_key_prefix': sort_key_prefix
    }
)

# Retrieve the queried items
items = response['Items']

# Print the queried attribute values
for item in items:
    attribute_value = item['attribute_name']
    print(attribute_value)'''