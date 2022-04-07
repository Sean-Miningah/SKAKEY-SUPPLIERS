from django.core.mail import send_mail
from django.conf import settings

def verification_email(email, verificationkey):
    SUBJECT = 'Verification of Account'
    FROM = settings.EMAIL_HOST_USER
    recipient = email
    message = 'Your key is: \n' + verificationkey
    send_mail(
        subject=SUBJECT,
        message=message,
        from_email=FROM,
        recipient_list=[recipient]
    )