import requests, sqlite3
from settings import TestUrl, BaseApiUrl, BaseUrl

# print(TestUrl)

# JsonData = requests.get(TestUrl)

# print(JsonData.text)


def LoadCourseNumbers():


    for CourseNumber in range(77125, 77130):
    # for CourseNumber in range(77153, 77200):
        CourseStringNumber = (str(CourseNumber).zfill(5))
        CheckUrl = (BaseUrl+CourseStringNumber+"?year=2026")
        ShnatonJson = requests.get(CheckUrl)

        CourceDict = {"Number":"Json"}
        print(CheckUrl)
        if (ShnatonJson.content == "b'[]'") == True:
            print("empty")
            print(requests.get(CheckUrl).content)
        else:
            print("not empty")
            print(requests.get(CheckUrl).content)

    
    # CourceDict.update({CourseStringNumber : requests.get(CheckUrl).content})

    print(CourceDict)
    return(CourceDict)

# test = LoadCourseNumbers()
# print(test)


TestEmptyJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/77126?year=2026")
TestFullJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/77129?year=2026")


print(str(TestEmptyJson.content) == "b'[]'")
print(str(TestFullJson.content) == "b'[]'")