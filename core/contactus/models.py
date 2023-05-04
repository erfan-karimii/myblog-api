from django.db import models

# Create your models here.
class contactModel(models.Model):
    STATUS = (
        ('Draft','Draft'),
        ("Publish","Publish"),
    )
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    massage = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS,default='Draft')
    

    def __str__(self):
        return self.name +" "+ self.subject