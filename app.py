import getpass
import smtplib
import csv

from email.mime.multipart import MIMEMultipart #Create email message object
from email.mime.text import MIMEText #To add html content onto mail

Host="smtp.gmail.com" #Responsible for sending email its the server.
Port=587 #Acts as virtual doorway to send mail from server to email client.
From_EMAIL="vedantpawar896@gmail.com"
Password=getpass.getpass("Enter the password: ")
#data=pandas.read_csv("Addresses.csv")
#To_EMAIL=data['email']
"""for i in To_EMAIL:
    smtp=smtplib.SMTP(Host,Port) #To set up server
    status_code, response=smtp.ehlo() #Pings the server and checks if its up and running
    print(f"Echoing: {status_code}, {response}")#To check if its working
    status_code, response=smtp.starttls()
    print(f"Start TLS: {status_code}, {response}")
    status_code, response=smtp.login(From_EMAIL, Password)
    print(f"Login: {status_code}, {response}")
    smtp.sendmail(From_EMAIL, i, message)
    smtp.quit()"""


with open("Addresses.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        #I can access row['email'] and row['name']
        message=MIMEMultipart("alternative") #Don't pass alternative as string parameter when sending plain text
        message['From']=From_EMAIL
        message['To']=row['email']
        message['Cc']=From_EMAIL
        message['Bcc']=From_EMAIL
        body='''Hi, {}
        
        How are you doing? This mail has been sent via python.
        From vedant'''.format(row['name'])
        message.attach(MIMEText(body, "plain"))

        #message=MIMEMultipart("alternative")
        #message['Subject']="Sending mail using python"
        #message['From']=From_EMAIL
        #message['To']=row['email']
        #message['Cc']=From_EMAIL
        #message['Bcc']=From_EMAIL

        #To read html file content and stor in a variable
        #html=""
        #with open("mailcontent.html","r") as file:
        #    html = file.read()
        #html_part=MIMEText(html, "html") #Used to convert plaintext into correct format
        #based on the mime type passed which in this case is "html".
        #Attach the html_part to message
        #message.attach(html_part)

        smtp=smtplib.SMTP(Host,Port) #To set up server
        status_code, response=smtp.ehlo() #Pings the server and checks if its up and running
        print(f"Echoing: {status_code}, {response}")#To check if its working
        status_code, response=smtp.starttls()
        print(f"Start TLS: {status_code}, {response}")
        status_code, response=smtp.login(From_EMAIL, Password)
        print(f"Login: {status_code}, {response}")
        smtp.sendmail(From_EMAIL, row['email'], message.as_string())
        smtp.quit()