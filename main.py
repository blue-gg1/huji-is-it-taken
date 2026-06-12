import requests, sqlite3
from settings import TestUrl, BaseApiUrl, BaseUrl

# print(TestUrl)

# JsonData = requests.get(TestUrl)

# print(JsonData.text)


def LoadCourseNumbers():


    for CourseNumber in range(77120, 77130):
    # for CourseNumber in range(77153, 77200):
        CourseStringNumber = (str(CourseNumber).zfill(5))
        # CheckUrl = (BaseApiUrl+"?year=2026&courseId="+CourseStringNumber)
        CheckUrl = (BaseUrl+CourseStringNumber+"?year=2026")
        CourceDict = {"Number":"Json"}
        print(CheckUrl)
        print(requests.get(CheckUrl).content)
        if requests.get(CheckUrl).content == "b'[]'":
            print("empty")
            print(requests.get(CheckUrl).content)
        else:
            print("not empty")
            print(requests.get(CheckUrl).content)

    
    # CourceDict.update({CourseStringNumber : requests.get(CheckUrl).content})

    print(CourceDict)
    return(CourceDict)

test = LoadCourseNumbers()
print(test)