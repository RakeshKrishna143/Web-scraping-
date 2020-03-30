import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
cases = soup.find('div',{'class':'maincounter-number'}).get_text().strip()
print(cases)

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 5 )
'''while True:
    notifyme('Total number of cases', cases)
    time.sleep(10) '''
print('s')
