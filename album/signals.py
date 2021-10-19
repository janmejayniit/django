from django.dispatch import receiver
from django.db.models import signals
from .models import Album
from django.conf import settings
from django.core.mail import send_mail


@receiver(signals.post_save, sender=Album)
def sendEmailToSubscriber(sender, instance, created, **kwargs):
    # print('Signal created for album.')
    subject = f'New image is uploaded by {instance.user}'
    message = 'Please go to website and watch newly created album.'
    email_from = 'Album Contest <{}>'.format(settings.EMAIL_HOST_USER)
    recipient_list = ['janmejay.py@yahoo.com', ]
    send_mail( subject, message, email_from, recipient_list )