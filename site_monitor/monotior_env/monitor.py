
import smtplib
import requests


r = requests.get('http://belabeast.de', timeout=5)

print(r)
if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('willywonkydony@gmail.com','frikadele97')

        subject = 'your ITB DUBLIN SITE is down '
        body = 'Try out to restart the server and its backing up'
        msg = f'Subject: {subject} \n\n {body}'

    
    smtp.sendmail('willywonkydony@gmail.com','willywonkydony@gmail.com',msg)
        

