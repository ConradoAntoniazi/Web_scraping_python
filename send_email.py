import smtplib
from email.message import EmailMessage

def send_email(nome, email, cardapio_ru):  
    msg = EmailMessage()

    msg['Subject'] = "CARDÁPIO DO RU"
    msg['From'] = 'webscrapingufes@gmail.com'
    msg['To'] = email
    password = 'ihjcxwxfvsaoxwsn'

    cardapio = cardapio_ru.replace('\n', '<br>')

    msg.add_header('Content-Type', 'text/html')
    email_content = f"""
    <p><b>===Cardápio RU===</b></p>
    <p>Olá {nome}! Este é o cardápio de hoje:<p>
    <p>{cardapio}</p>
    """
 
    msg.set_content(email_content, subtype='html')

    try:
        with smtplib.SMTP('smtp.gmail.com: 587') as s:
            s.starttls()
            s.login(msg['From'], password)
            s.send_message(msg)
            print("Email enviado com sucesso!")
    except smtplib.SMTPAuthenticationError:
        print("Falha na autenticação. Verifique o usuário e a senha.")
    except Exception as e:
        print(f"Erro durante o envio de e-mail: {e}")
