from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
email = models.EmailField()
phone = models.CharField(max_length=20)


class Device(models.Model):
client = models.ForeignKey(Client, on_delete=models.CASCADE)
brand = models.CharField(max_length=100)
model = models.CharField(max_length=100)
serial_number = models.CharField(max_length=100)


class Repair(models.Model):
STATUS_CHOICES = [
('NEW', _('Nowe')),
('IN_PROGRESS', _('W trakcie')),
('DONE', _('Gotowe')),
]


device = models.ForeignKey(Device, on_delete=models.CASCADE)
description = models.TextField()
status = models.CharField(max_length=20, choices=STATUS_CHOICES)
estimated_cost = models.DecimalField(max_digits=8, decimal_places=2)
