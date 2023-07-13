import imp
from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email,email_token):
    subject = 'Your account needs to be verified'#subject of the e-mail
    email_from = settings.EMAIL_HOST_USER #ALREADY EXISTING feature in django to send emails
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'#stating which message to print and 
    send_mail(subject , message , email_from , [email])#email list jayega