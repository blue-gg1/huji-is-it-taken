import requests
from settings import TestUrl, BaseApiUrl

# print(TestUrl)

# JsonData = requests.get(TestUrl)

# print(JsonData.text)

for CourseNumber in range(77000, 80000):
    CourseStringNumber = (str(CourseNumber).zfill(5))
    CheckUrl = (BaseApiUrl+"?year=2026&"+CourseStringNumber)
    print(CheckUrl)
    print(requests.get(CheckUrl).content)