from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_aurthor = models.CharField(max_length=50)
    book_drscription = models.TextField()

    

# Create your models here.
