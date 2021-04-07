import requests
import webbrowser
from bs4 import BeautifulSoup
import datetime
import sys


portNumber = input()
try:
   val = int(portNumber)
except ValueError:
   sys.exit("Not a port number.")

URL = 'https://www.marinetraffic.com/bg/ais/details/ports/' + portNumber
agent = {"User-Agent":'Mozilla/5.0'}
page = requests.get(URL, headers=agent).text
source = str(page)

soup = BeautifulSoup(source, 'html.parser')
try:
   portName = soup.find('h1', class_ = 'font-220 no-margin').text
except AttributeError:
   sys.exit("Not a port number.")

country = soup.find('span', class_= 'font-120').text
shipsOnThePortCount = soup.find('div', class_= 'bg-info bg-light padding-10 radius-4 text-left').text

file = open("pD.txt", "a")
file.write('Port Name: ' + str(portName).split(' ')[0] + '\n')
file.write('Port number(MarineTraffic)' + ': ' + portNumber + '\n')
file.write('Country: ' + str(country).split(' ')[1] + '\n')
file.write('Coordinates:  ' + (str(shipsOnThePortCount).replace('\n', '~')).split('~')[3] + '\n')
file.write('All the ships on the port on '+ (str(datetime.datetime.now()).split(':')[0] + ':' + str(datetime.datetime.now()).split(':')[1]) + ' are: ' + (str(shipsOnThePortCount).replace('\n', '~')).split('~')[18] + '\n')
file.write('Un/lcode: ' + (str(shipsOnThePortCount).replace('\n', '~')).split('~')[14] + '\n')
file.write('~~~~' + '\n')
file.close()