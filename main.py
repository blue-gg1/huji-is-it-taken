import requests
from settings import TestUrl, BaseApiUrl

# print(TestUrl)

# JsonData = requests.get(TestUrl)

# print(JsonData.text)

for CourseNumber in range(0, 10000):
    CourseStringNumber = (str(CourseNumber).zfill(5))
    CheckUrl = (BaseApiUrl+"?year=2026&"+CourseStringNumber)
    print(CheckUrl)
    print(requests.get(CheckUrl).content)