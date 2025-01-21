from fastapi_mail import ConnectionConfig


conf = ConnectionConfig(
    MAIL_PORT=465, 
    MAIL_SERVER="smtp.mail.ru",  
    MAIL_USERNAME="info@paketon.com", 
    MAIL_PASSWORD="biwyPFucHLTj3tASnFbr", 
    MAIL_FROM="info@paketon.com", 
    MAIL_STARTTLS=False, 
    MAIL_SSL_TLS=True, 
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

conf2 = ConnectionConfig(
    MAIL_PORT=465, 
    MAIL_SERVER="smtp.mail.ru",  
    MAIL_USERNAME="fr@paketon.com", 
    MAIL_PASSWORD="k5P0xCtmLrrXczv2e6e5", 
    MAIL_FROM="fr@paketon.com", 
    MAIL_STARTTLS=False, 
    MAIL_SSL_TLS=True, 
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
