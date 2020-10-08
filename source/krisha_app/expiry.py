import datetime as dt
import time
import smtplib
from django import views



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    email_user = 'yuvaram2012@gmail.com'
    email_pass = 'RRAHX001'
    receiver = 'yuvaram2012@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_user, email_pass)

    # EMAIL
    message = ''
    server.sendmail(email_user, receiver, message)
    server.quit()



def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

first_email_time = dt.datetime(2020,9,15,15,5,0) # set your sending time in UTC
interval = dt.timedelta(minutes=1) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval