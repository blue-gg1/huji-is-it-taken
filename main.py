import requests
from settings import TestUrl

print(TestUrl)

JsonData = requests.get(TestUrl)

print(JsonData.text)