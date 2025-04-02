import requests
import os
API_KEY = "b6cbadc4b7f1f817222ec5bc40c529b51d2a4a01e4c8c5f192ba90cb5bc06bfc"
file_path = "count in file.py"
url ='https://www.virustotal.com/vtapi/v2/file/scan'
params_post = {"apikey" : API_KEY}
with open(file_path, "rb") as file:
    files = {'file': file}
    response = requests.post(url, data=params_post, files=files)
    if response.status_code == 200:
        if response.headers['Content-Type'] == 'application/json':
            response_json = response.json()
            resource = response_json['resource']
            params_get ={"apikey":API_KEY, "resource" : resource}
            response = requests.get(url, params_get )
            if response.status_code == 200:
                if r.headers['Content-Type'] == 'application/json':
                    
            else:
                print("Error, the file didnt send successfullt to virus total :(") 
    else:
        print("Error, the file didnt send successfullt to virus total :(") 