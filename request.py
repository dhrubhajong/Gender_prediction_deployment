import requests

url = 'http://localhost:5000/predict_api'

#url='http://127.0.0.1:5000/predict_api'
data=   {
         'left canine width intraoral',
         'left canine width casts',
         'right canine width casts' 
         'right canine width intraoral',
         'intercanine distance casts',
         'left canine index casts'
         }
response=requests.post(url,json=list(data))
print(response.json())