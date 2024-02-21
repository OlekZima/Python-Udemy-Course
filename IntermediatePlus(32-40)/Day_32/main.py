import smtplib as smtp
from credentials import my_email, app_password, mail_send

connection = smtp.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=app_password)  # type: ignore
connection.sendmail(from_addr=my_email, to_addrs=mail_send, msg="Hello")  # type: ignore

connection.close()
