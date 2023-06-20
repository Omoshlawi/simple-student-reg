from django.db import models

# Create your models here.


class Students(models.Model):
    tt_number = models.CharField(max_length=50, primary_key=True)
    results = models.CharField(max_length=50)
    verified = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='verified')