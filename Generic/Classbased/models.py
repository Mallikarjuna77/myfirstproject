from django.db import models

class Cracker(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Weight=models.IntegerField()
    Height=models.IntegerField()

    def __str__(self):
        return self.Name

