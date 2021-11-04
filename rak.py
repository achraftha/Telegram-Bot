import requests
import datetime
import xmltodict, json
from bs4 import BeautifulSoup


def getMenuforDay(day,nextDay):
  r = requests.get('http://services.imt-atlantique.fr/rak/')
  print("this is the respose" ,r.encoding)
  obj=xmltodict.parse(r.text, encoding='UTF-8')
  BigList=[]
  soup=BeautifulSoup(obj['rss']['channel']['item'][1]['description'],'lxml')
  for link in soup.find_all('a'):
    BigList.append(link.string)

  # print(BigList)
  stringToSend=''
  dayIndexInlist=BigList.index(day.capitalize())
  nextDayIndexInList=BigList.index(nextDay.capitalize())
  for i in range(dayIndexInlist+1,nextDayIndexInList):
    stringToSend=stringToSend+BigList[i]+'\n'
  return stringToSend