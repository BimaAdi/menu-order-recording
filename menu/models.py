from django.db import models

# Create your models here.
class Menu(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = 'menu'
