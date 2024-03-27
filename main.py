from urllib.request import urlopen
from urllib.error import URLError
import xml.etree.ElementTree as ET


def getURL():
    url = input("Enter the RSS URL: ")
    return url

def readURL(url):
    try:
        data = urlopen(url).read()
        return data
    except URLError as e:
        print("Error occurred:", e)
        return None


def parseRSS(data):
    tree = ET.fromstring(data)
    item = tree.find('.//item')

    title = item.find("title").text
    description = item.find("description").text
    url = item.find("link").text 

    print("Title =",title)
    print("Description =",description)
    print("URL =",url)

    
def main():    
    url = getURL()
    data = readURL(url)
    if data:
        parseRSS(data)


if __name__ == "__main__":
    main()

