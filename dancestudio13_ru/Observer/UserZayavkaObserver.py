from email import charset
from dancestudio13_ru.Data.Config import Config

import smtplib
import email.message
import datetime

class UserZayavkaObserver:

    def sendEmailAboutNewToAdmin(self, name: str, phone: str, ip_address: str, date_of_add: str) -> bool:
        email_content = '''
        <html>
        <head>
            <meta charset="utf-8">
            <title>Сообщение с сайта 13danceonline.ru</title>
        </head>
        <body>
            <h2>Сообщение с сайта 13danceonline.ru</h2>
            <p><b>Дата сообщения:</b> ''' + str(date_of_add) +''' </p>
            <p><b>Имя:</b> ''' + name +''' </p>
            <p><b>Номер телефона:</b> ''' + phone +''' </p>
            <p><b>IP-адрес:</b> ''' + ip_address +''' </p>
        </body>
        </html>
        '''

        msg = email.message.Message()
        msg['Subject'] = 'Сообщение с сайта 13danceonline.ru'
        
        msg['From'] = Config.SMTPEmailLogin
        msg['To'] = Config.adminEmail
        
        ...

        return True
