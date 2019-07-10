import requests
import bs4
import smtplib



def send_mail(list):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('rakesh1432rakei@gmail.com','cnnywsosuceizgwo')

    sub = 'hello Madhan!'
    body=''
    for i in range(len(list)):
        body += list[i][0] + '\n'+ list[i][1] +' '+ list[i][2] + '\n'
    msg = 'Subject: '+sub+'\n\n'+body
    print(msg)

    server.sendmail('rakesh1432rakei@gmail.com','madhansugumar@gmail.com',msg)
    server.quit()
    print('mail sent!')


def seperate(a):
    a= a.strip()
    a=a.split()
    if len(a)==5:
        a[0]=a[0]+a[1]
        del a[1]
    team = a[0]+' '+a[1]
    run = a[2]
    over = a[3]
    return [team,run,over]



link = 'https://www.cricbuzz.com/live-cricket-scorecard/20282/ind-vs-nz-1st-semi-final-1-v-4-icc-cricket-world-cup-2019'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text,'html.parser')
details = soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
list=[]
for i in range(len(details)-1):
    a=details[i].getText()
    list.append(seperate(a))
print(list)
send_mail(list)
