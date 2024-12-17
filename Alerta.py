import requests 
import smtplib
import email.message

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

requisicao_dicionario = requisicao.json()

cotacao = float(requisicao_dicionario['USDBRL']['bid'])

print(cotacao)

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Dolar está abaixo de R$5.50 Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dolar abaixo de R$5.20"
    msg['From'] = '' #Insira o email do remetente
    msg['To'] = ''   #Insira o email do destinatario
    password = ''    #Acesse a aba "senhas de app" no seu gmail gere uma senha e cole aqui
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


if cotacao < 6.50:
   enviar_email(cotacao)