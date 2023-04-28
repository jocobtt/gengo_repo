import requests
import json

my_headers = {'apiKey': '33f078ff-6efa-4271-be28-e7f140d93de9'}
response = requests.get('https://dcmetrohero.com/api/v1/metrorail/trains', headers =my_headers)
#print(response.json())
data = response.text
parse_json = json.loads(data)
print(parse_json)
