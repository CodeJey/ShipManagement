import requests
import webbrowser
from bs4 import BeautifulSoup
import datetime
import sys

#Четем номера на пристанище и обработваме входа с хващане на грешка
portNumber = input()
try:
   val = int(portNumber)
except ValueError:
   sys.exit("Not a port number.")

# Тук се обработва формирането на url-a 
URL = 'https://www.marinetraffic.com/bg/ais/details/ports/' + portNumber
# Агент за подвеждане на страницата, която има защита от scrapers
agent = {"User-Agent":'Mozilla/5.0'}
# тук си вземаме сорса на страницата и го кастваме за стринг за по-сигурно 
page = requests.get(URL, headers=agent).text
source = str(page)
# Тук се прави "супа", която се изразява в структуриране на получения сорс като html
# за да може да се работи с елементи и съдържание
soup = BeautifulSoup(source, 'html.parser')
# хващане на ексепшън в случай, че не се намери търсеното нещо
# например когао се въведе число 2 за номер на пристанище не ни препраща към нищо
# защото няма пристанище с номер 2, в този случай се хвърля AttributeError, която улаваме тук
try:
   # Взема се името по елент
   portName = soup.find('h1', class_ = 'font-220 no-margin').text
except AttributeError:
   sys.exit("Not a port number.")

shipURL = 'https://www.marinetraffic.com/bg/data/?asset_type=vessels&columns=flag,shipname,photo,recognized_next_port,reported_eta,reported_destination,current_port,imo,ship_type,show_on_live_map,time_of_latest_position,lat_of_latest_position,lon_of_latest_position,notes&current_port_in|begins|' + str(portName).split(' ')[0] + '|current_port_in=' + portNumber
# взема се държава и колко кораба има там(не се обработва като ексепшън, защото ако намерим име ще има и другите неща)
country = str(soup.find('span', class_= 'font-120').text)
# този код реално взема колко кораба са на пристанището, координати, код на пристанище и ояаквани кораби, както и точно време там
shipsOnThePortCount = soup.find('div', class_= 'bg-info bg-light padding-10 radius-4 text-left').text


# Тук се пише във файла
# отваряне на файла
file = open("pD.txt", "a")
# Вземаме само името на пристанището
file.write('Port Name: ' + str(portName).replace(portName.split(' ')[len(portName.split(' ')) - 1], '') + '\n')
# Ще му изписваме и кода, който сме въвели
file.write('Port number(MarineTraffic)' + ': ' + portNumber + '\n')
# страна
file.write('Country:' + country.replace(country.split(' ')[0], '') + '\n')
# координатите се обработват и пишат 
file.write('Coordinates(w/l): ' + ((str(shipsOnThePortCount).replace('\n', '~')).split('~')[3]).replace("°", "deg") + '\n')
# брой кораби се обработва и пише
file.write('All the ships on the port on '+ (str(datetime.datetime.now()).split(':')[0] + ':' + str(datetime.datetime.now()).split(':')[1]) + ' are: ' + (str(shipsOnThePortCount).replace('\n', '~')).split('~')[18] + '\n')
# Кода се добавя
file.write('Un/lcode: ' + (str(shipsOnThePortCount).replace('\n', '~')).split('~')[14] + '\n')
# добавя се финален ред със символите за отделяне
file.write('~~~~' + '\n')
# затваряме файла
file.close()

# webbrowser.open_new_tab(shipURL)
