from django.db import models

# Create your models here.
class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name +" - "+ str(self.id)