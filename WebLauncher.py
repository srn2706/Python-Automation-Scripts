import urllib.request
from sys import *
import webbrowser
import re
from urllib.request import urlopen


def is_connected():
    try:
        urllib.request.urlopen('https://www.google.co.in/', timeout=1)
        return True
    except Exception as err:
        print("Error : ",err)
        return False


def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url


def Weblauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new = 2)

def main():
    print("Application name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("this Script is used open URL which are written in one file")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : Application_Name Name_OF_File")
        exit()

    try:
        connected = is_connected()

        if connected:
            Weblauncher(argv[1])
        else:
            print("Unable to connect to Internet...")

    except ValueError:
        print("Error : Invalid datatype of Input")
    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()