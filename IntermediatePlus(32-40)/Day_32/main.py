import smtplib as smtp
from credentials import my_email, app_password, mail_send

with smtp.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)  # type: ignore
    connection.sendmail(
        from_addr=my_email,
        to_addrs=mail_send,
        msg="Subject:Greetings\n\nMy email for myself via smtp and python.",
    )  # type: ignore
