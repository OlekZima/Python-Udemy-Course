import smtplib as smtp
from quote_sender.credentials import my_email, app_password, mail_send

with smtp.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=mail_send,
        msg="Subject:Greetings\n\nMy email for myself via smtp and python.",
    )
