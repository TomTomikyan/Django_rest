from django.db import models

# Create your models here.

class category(models.Model):

    name = models.CharField('name',max_length=250)
    img = models.ImageField('image',upload_to='category/')

    def __str__(self) -> str:
        return self.name
    
class car(models.Model):

    category = models.ForeignKey(category,on_delete=models.CASCADE,related_name='car')
    name = models.CharField('name ',max_length=250)
    img = models.ImageField('image',upload_to='car/')

    def __str__(self) -> str:
        return self.name