import boto3

client = boto3.client('organizations')

# The following example shows you how to request a list 
# of the accounts in an organization:
response = client.list_accounts(
)
print(response)

# Retrieves Organizations-related information about the specified account. 
# AccountId=your.role.account.id)
response = client.describe_account(
    AccountId='342055123193'
)

