from django.db import models
from datetime import datetime

# Create your models here.


class Investimento(models.Model):
    investimento = models.TextField(max_length=25)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    
