import smtplib, ssl
import secrets


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = secrets.getusername()
    password = secrets.get_password()

    receiver = secrets.get_receiver()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
