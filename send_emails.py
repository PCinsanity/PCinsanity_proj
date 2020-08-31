import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# email details
email = "your email"
password = "your password"
target_email = "target email"
subject = "Hello"
message = f"Hello {target_email.split('@')[0]}"
# {target_email.split('@')[0] gets the first part of the email (e.g hello@gmail.com, the command gets 'hello')

# creating message
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = target_email
msg['Subject'] = subject
# adding your message
msg.attach(MIMEText(message, 'plain'))

# sending your message
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()   # place  SMTP connection in TLS (Transfer Layer Security) mode
server.login(email, password)
text = msg.as_string()
server.sendmail(email, target_email, text)
