from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    people=models.IntegerField(null=True)

    def __str__(self):
        return(self.name)