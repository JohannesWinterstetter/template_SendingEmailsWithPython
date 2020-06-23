#description: template for sending an mail from a gmail account
#instruction: fill in the your data in lines 14 to 18 and the location of your attachement in line 27
#author: Johannes Winterstetter

#import the needed modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#create a function for sending the mail
def f_send_the_data():
    email = 'YOUR_GMAIL_ADDRESS@gmail.com'
    password = 'YOUR_PASSWORD'
    send_to_email = 'WHO_WILL_GET_THE_MAIL'
    subject = 'SUBJECT'
    message = 'TEXT123'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    #optional: comment this paragraph in case you are not wanting to send an attachement
    msg.attach(MIMEText(message, 'plain'))
    file_location = 'LOCATION'
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()

#send a mail with the function
f_send_the_data()