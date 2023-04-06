import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



EMAIL_ADDRESS = 'test@test.test'
destinataire = 'target@gmail.com'

# SMTP server information
SMTP_SERVER = 'srrv_smtp'
SMTP_PORT = 25

# Create the email message
msg = MIMEMultipart()
msg['From'] = EMAIL_ADDRESS
msg['To'] = destinataire
msg['Subject'] = 'Test Email'

# Add a text message to the email
body = 'This is a test email sent from Python.'
msg.attach(MIMEText(body, 'plain')) #<-replacer plain par html pour avoir le msg en html 

#Pour pièce jointe :

#filename = 'example.txt'
#with open(filename, 'r') as f:
#    attachment = MIMEText(f.read())
#    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
#    msg.attach(attachment)

# Connect to the SMTP server and login
print("Connecting to server")
smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
print("Sending message to", destinataire, "as", EMAIL_ADDRESS)
smtp_server.sendmail(EMAIL_ADDRESS, destinataire, msg.as_string())
print("Mail sent succesfully")

# Disconnect from the SMTP server
smtp_server.quit()
