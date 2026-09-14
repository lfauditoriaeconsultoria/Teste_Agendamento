import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém as credenciais e configurações
email_remetente = os.getenv("EMAIL_REMETENTE")
senha = os.getenv("EMAIL_SENHA")
email_destinatario = os.getenv("EMAIL_DESTINATARIO")
smtp_porta = int(os.getenv("SMTP_PORTA", "587"))
smtp_host = os.getenv("SMTP_HOST")

# Configuração do e-mail
assunto = "E-mail de teste - Python"

corpo = """
Olá!

Este é um e-mail de teste enviado automaticamente
por meio de um código em Python.

"""

# Cria a mensagem
mensagem = MIMEMultipart()
mensagem["From"] = email_remetente
mensagem["To"] = email_destinatario
mensagem["Subject"] = assunto

# Adiciona o corpo do e-mail
mensagem.attach(MIMEText(corpo, "plain", "utf-8"))

try:
    # Conecta ao servidor SMTP
    with smtplib.SMTP(smtp_host, smtp_porta) as servidor:

        # Inicia a conexão segura
        servidor.starttls()

        # Realiza o login
        servidor.login(email_remetente, senha)

        # Envia o e-mail
        servidor.sendmail(
            email_remetente,
            email_destinatario,
            mensagem.as_string()
        )

    print("E-mail enviado com sucesso!")

except Exception as erro:
    print(f"Erro ao enviar o e-mail: {erro}")