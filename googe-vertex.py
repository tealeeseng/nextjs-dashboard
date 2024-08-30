import base64
import json

with open('path/to/your/service-account-file.json', 'r') as file:
    service_account_info = file.read()

encoded_key = base64.b64encode(
    service_account_info.encode('utf-8')).decode('utf-8')
print(encoded_key)
