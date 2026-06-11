import requests
from settings import TestUrl, BaseApiUrl, BaseUrl

# print(TestUrl)

# JsonData = requests.get(TestUrl)

# print(JsonData.text)

for CourseNumber in range(77153, 80000):
    CourseStringNumber = (str(CourseNumber).zfill(5))
    # CheckUrl = (BaseApiUrl+"?year=2026&courseId="+CourseStringNumber)
    CheckUrl = (BaseUrl+CourseStringNumber+"?year=2026")
    print(CheckUrl)
    print(requests.get(CheckUrl).content)