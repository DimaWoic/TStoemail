import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(addr_to, body):

    addr_from = "svgetbot@yandex.ru"
    #addr_to = "maksim.filin@inbox.ru"

    password = "zxcvbnM123"

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Событие ТС'

    #body = "Включился фидер Профсоюзный"
    msg.attach(MIMEText(body, 'plain'))

    html = """\
<html>
  <head></head>
  <body>
    <p>
       Фрагмент HTML-кода
    </p>
  </body>
</html>
"""
    #msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.yandex.com', 587)
    #server.set_debuglevel(True)
    tls = server.starttls()
    print(tls)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

#msg = "ПСТ № 4 Включился фидер Рижский"
#send_mail("maksim.filin@inbox.ru", msg)
#send_mail("wdv85@mail.ru", msg)
#send_mail("o_vasilev@bk.ru", msg)
