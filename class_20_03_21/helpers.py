from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from class_20_03_21.models import DB_NAME
import smtplib, ssl

def get_session():
    engine = create_engine(f'sqlite:///{DB_NAME}')
    Session = sessionmaker(bind=engine)
    return Session()


def send_email_for(new_restaurants=[]):
    passwd = input('Password: ')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', context=context, port=465) as smtp_server:
        smtp_server.login('programmingangela@gmail.com', password=passwd)
        message = MIMEMultipart("html_message")
        message['Subject'] = "Restaurants"

        content_text = MIMEText("Text 123", "text")
        content_html = MIMEText("<h1>Text 123</h1>", "html")
        message.attach(content_html)
        message.attach(content_text)
        smtp_server.sendmail(from_addr='programmingangela@gmail.com',
                             to_addrs=['programmingangela@gmail.com'],
                             msg=message.as_string())


if __name__ == '__main__':
    send_email_for()



