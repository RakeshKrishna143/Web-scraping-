import requests
import bs4
import smtplib



def send_mail(team,run,wicket):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rakesh1432rakei@gmail.com','cnnywsosuceizgwo')

    sub = 'hello Madhan!'
    body = team + '\n'+ run +'\n'+ wicket
    msg = 'Subject: '+sub+'\n\n'+body
    print(msg)

    server.sendmail('rakesh1432rakei@gmail.com','madhansugumar@gmail.com',msg)
    server.quit()
    print('mail sent!')

link = 'https://www.cricbuzz.com/live-cricket-scorecard/20282/ind-vs-nz-1st-semi-final-1-v-4-icc-cricket-world-cup-2019'
res = requests.get(link)
print(res)
soup = bs4.BeautifulSoup(res.text,'html.parser')
name = soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
a=name[0].getText()
a= a.strip()
print(a)
a=a.split()
print(a)
if len(a)==5:
    a[0]=a[0]+a[1]
    del a[1]
team = a[0]+' '+a[1]
run = a[2]
wicket = a[3]
print(team,run,wicket)
send_mail(team,run,wicket)
