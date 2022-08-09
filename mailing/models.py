from http import client
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
import requests

from fabrique.service import MailingProcess
# Create your models here.

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    text = models.CharField(max_length=256)
    filter = models.CharField(max_length=256) # в формате "code_tag"
    end_time = models.DateTimeField()


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    telephon_number = models.IntegerField()
    operator_code = models.IntegerField()
    tag = models.CharField(max_length=256)
    time_zone = models.CharField(max_length=256)

class Message(models.Model):
    MESSAGE_STATUS = (
        ('S', 'sent'),
        ('R', 'recieved')
    )
    id = models.AutoField(primary_key=True)
    send_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=MESSAGE_STATUS) # только 2 вожможных статуса
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)






@receiver(post_save, sender=Mailing)
def send_appointment_confirmation_email(sender, instance, created, **kwargs):
  if created:
        clients = Client.objects.all()
        code, tag = instance.filter.split()
        for c in clients:
            if c.tag == tag and c.operator_code == int(code):
                new_message = Message.objects.create(send_time = datetime.now(), status = 'S', mailing_id=instance, client_id=c)
                service = MailingProcess()
                service.send_message(instance, new_message, c)
                