import sys
import json


if __name__ == '__main__':
    scanId =  int(sys.argv[1])
    file = open("./site-assets.json","rt")
    content = file.read()
    content =  json.loads(content)["resources"]
    file.close()
    #print(content)
    for obj1 in content:
        for obj2 in obj1["history"]:
            if (obj2["scanId"] == scanId ) and (obj1["vulnerabilities"]["critical"]>0):
                print(obj1["ip"])