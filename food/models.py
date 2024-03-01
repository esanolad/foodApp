from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=350)
    item_price = models.IntegerField()
    
    def __str__(self):
        return self.item_name
    
    