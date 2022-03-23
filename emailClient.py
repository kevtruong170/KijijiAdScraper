import smtplib
import emailTemplate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Input your email
email = ""
#Input your password
password = ""
#Reading in email template
message_template = emailTemplate.read_template('messageTemplate.txt')

#Logging onto email client server
def eLogin():
    try:
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(email, password)
        return s
    except:
        print("Error starting SMTP")
        return None

#Sends email
def sendEmail(listing, userEmail):
    msg = MIMEMultipart()

    #Utilizes email template to format car listings
    message = message_template.substitute(AD_TITLE=listing.title, AD_PRICE=listing.price,
                                          AD_LOCATION=listing.location, AD_DESC=listing.description,
                                          AD_LINK=listing.link)
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = listing.title
    msg.attach(MIMEText(message, 'plain'))
    userEmail.send_message(msg)
    del msg