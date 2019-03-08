from django.db import models

# Create your models here.
class GarageSell(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    imageURL=models.CharField(max_length=200)

    def __str__(self):
        return self.name