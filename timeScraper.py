import re, os
from bs4 import BeautifulSoup
import urllib.request

os.system("clear")
url = 'https://www.timeanddate.com/worldclock/?query='
city = input("Enter the city to find time and weather: ")
city1 = re.sub(' ', '+', city)
link = url + city1
m = urllib.request.Request(link)
html = urllib.request.urlopen(m)
soup = BeautifulSoup(html, "html.parser")
allLinks = soup.find_all('td', {"class": "rbi"})
currentTime = re.findall(r'\d', allLinks[0].string)
currentTime = [str(item) for item in currentTime]

hh = int(currentTime[0] + currentTime[1])
mm = int(currentTime[2] + currentTime[3])

if hh >= 12:
	amOrPm = "PM"
	if hh != 12:
		hh = hh - 12
elif hh < 12:
	amOrPm = "AM"

print ("Time in " + city + " is " + str(hh) + ":" + str(mm) + " " + amOrPm)