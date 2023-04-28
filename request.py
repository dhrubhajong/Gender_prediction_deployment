import requests

url = 'http://localhost:5000/predict_api'


data = {'left canine width intraoral': left canine width intraoral,
        'left canine width casts': left canine width casts,
        'right canine width casts' : right canine width casts,
        'right canine width intraoral': right canine width intraoral,
        'intercanine distance casts' : intercanine distance casts,
        'inter canine distance intraoral': inter canine distance intraoral}

response= request.post(url,files=data)
