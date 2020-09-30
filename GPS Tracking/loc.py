import requests
import json


url = 'http://ipinfo.io/json'
a = requests.get(url)
#print(a.text)

data = a.json()

#print(data)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
loc=data['loc']

print("city:"+ city)
print("region: "+ region)
print("country: "+ country)
print("lat,long: "+ loc)