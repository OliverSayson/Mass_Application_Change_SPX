import requests

def read_client_secrets(file_path):
    client_secrets = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            client_secrets[key] = value
    return client_secrets

# Read client secrets
client_secrets = read_client_secrets('/Users/oliver/client.txt')

headers1 = {
    'content-type': 'application/x-www-form-urlencoded',
}

data = {
  'client_secret': client_secrets['client_secret'],
  'client_id': client_secrets['client_id'],
  'grant_type': 'client_credentials'
}

response = requests.post('https://auth.smaato.com/v2/auth/token/', headers=headers1, data=data)
v = response.json()
w = v['access_token']

url_base = 'https://spx-api.smaato.com/publisherportal/api/inventory/v1/applications/'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(w)}

publisher_ids = ['1100052485','1100052485','1100052485']
app_ids = ['121146601',
'121146819',
'121146983']
#categories = []

for (app_id,
     headers['x-spx-publisher-id']
     #category
     ) in zip(app_ids, publisher_ids
    #, categories
    ):
    url = url_base + app_id
    response = requests.get(url, headers=headers)
    json_data = response.json()
    #json_data['category'] = category
    put_response = requests.get(url, headers=headers, json=json_data)
    print(put_response.json())
