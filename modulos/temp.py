from string import Template
from datetime import datetime
from dadosEmail import myEmail, mySenha
from email.mime.multipart import MIMEMultipart #Destinatário e remetente
from email.mime.text import MIMEText #Corpo do email
from email.mime.image import MIMEImage #Imagens
import smtplib

with open("modulos\zemplate.html", 'r') as html:
    template = Template(html.read())
    dataAtual = datetime.now().strftime('%d/%m/%Y')
    corpoMsg = template.substitute(
        nome="Caio Faiad", data=dataAtual, email="profcaiofaiad@gmail.com", lang="Python")

msg = MIMEMultipart()
msg['From'] = "Mateus Henrique Silva e Silva"
msg['To'] = "profcaiofaiad@gmail.com"
msg['Subject'] = 'Atenção: este é um e-mail de testes.'


corpo = MIMEText(corpoMsg, 'html')
msg.attach(corpo)


"""
A sigla SMTP significa Simple Mail Transfer Protocol, o que na tradução para o português fica algo próximo a “Protocolo Simples de Transferência de Correio”. Apesar de ser instantâneo e quase automático, sem esse protocolo da internet não seria possível mandar mensagens e se comunicar com outros servidores de e-mail.
"""


with smtplib.SMTP(host='smtp.gmail.com', port=587,) as smtp:
#    smtp.ehlo()
    smtp.starttls()
    smtp.login(myEmail, mySenha)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string().encode('UTF-8'))
    print('Email enviado com sucesso')
