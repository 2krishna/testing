from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives

# from testapp.token import user_tokenizer
from django.utils.html import strip_tags


def send_confirmation_mail(user):
    token = user_tokenizer.make_token(user)
    mail_subject = 'Activate your account.'
    user_dict = {
        'user': user,
        'domain': 'https://www.newjobshub.com/',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token,
    }
    message = render_to_string('mail_confirmation_message.html', user_dict)
    plain_message = strip_tags(message)
    to_email = user.email
    msg = EmailMultiAlternatives(mail_subject, plain_message, 'noreply@newjobshub.com', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()
    return True


def send_welcome_mail(user):
    # token = user_tokenizer.make_token(user)
    mail_subject = 'Welcome'
    user_dict = {
        'user': user,
        'domain': 'https://www.newjobshub.com/',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        # 'token': token,
    }
    message = render_to_string('testapp/welcome.html', user_dict)
    plain_message = strip_tags(message)
    # to_email = user.email
    to_email = 'krishnakashyap.balj@gmail.com'
    msg = EmailMultiAlternatives(mail_subject, plain_message, 'noreply@newjobshub.com', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()
    return True


def send_reset_password_mail(user):
    token = user_tokenizer.make_token(user)
    mail_subject = 'Reset your password'

    user_dict = {
        'user': user,
        'domain': 'https://www.newjobshub.com/',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token,
    }
    message = render_to_string('reset_password.html', user_dict)
    plain_message = strip_tags(message)
    to_email = user.email
    msg = EmailMultiAlternatives(mail_subject, plain_message, 'noreply@newjobshub.com', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()

    send_mail(mail_subject, message, 'noreply@newjobshub.com', [to_email])

    return True



