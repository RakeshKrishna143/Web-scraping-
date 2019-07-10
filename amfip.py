import requests
import bs4
import smtplib


def send_mail():
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('rakesh1432rakei@gmail.com','cnnywsosuceizgwo')

    s.sendmail('rakesh1432rakei@gmail.com','rakesh1432rakie@gmail.com',msg)
    s.quit()
    print('mail sent!')
#link = 'https://www.flipkart.com/redmi-note-7-pro-neptune-blue-128-gb/p/itmffdudreuhph5y?pid=MOBFDXZ3Z8WBPDWK&srno=s_1_1&otracker=search&otracker1=search&lid=LSTMOBFDXZ3Z8WBPDWKZPE9BP&fm=SEARCH&iid=643eaf13-204b-423b-9332-b0fcc83e69a6.MOBFDXZ3Z8WBPDWK.SEARCH&ppt=sp&ppn=sp&ssid=3lu4rzj2e80000001562773467493&qH=9b6bf0057c19bd94'
link = 'https://www.amazon.in/dp/B07D1GS2KQ?aaxitk=BC3Xeu59yRSvrQfQ0JEF1g&pd_rd_i=B07D1GS2KQ&pf_rd_p=65eb14ef-a10e-4be0-99be-a4c4b70ff707&hsa_cr_id=4095363360202&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F91RHqhXsEaL.jpg&sb-ci-a=B07D1GS2KQ'
#link = "https://www.amazon.in/Apple-MacBook-13-inch-Retina-Quad-Core/dp/B07FLGJ89V/ref=sr_1_1?crid=A8H94M4CME40&keywords=mac+books+pro&qid=1562770392&s=gateway&sprefix=mac+boo%2Caps%2C330&sr=8-1"
#link = 'https://www.amazon.in/Redmi-Pro-Black-64GB-Storage/dp/B07DJHXWZZ/ref=sr_1_1?crid=2YHJIOSI6WZV2&keywords=note+6+pro&qid=1562770176&s=gateway&sprefix=note+%2Caps%2C1035&sr=8-1'
#header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

res = requests.get(link,headers=header)
print(res)
soup= bs4.BeautifulSoup(res.text,'lxml')
#print(soup.find('div',{'class':'_1vC4OE _3qQ9m1'}))
print(soup.find('span',{'id':'priceblock_ourprice'}))
