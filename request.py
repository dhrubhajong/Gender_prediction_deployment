from flask import request
import requests

url = 'http://localhost:5000/predict_api'


data = ('left canine width intraoral',
        'left canine width casts',
        'right canine width casts' ,
        'right canine width intraoral',
        'intercanine distance casts',
        'inter canine distance intraoral')

response= requests.post(url,json=list(data))
