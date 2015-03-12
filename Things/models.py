from django.db import models


# Create your models here.
class Color(models.Model):
    enName = models.CharField(verbose_name='Name', max_length=200, blank=False, help_text='enter a value')
    description = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.enName

class Shape(models.Model):
    enName = models.CharField(verbose_name='Name', max_length=200, blank=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.enName

class Thing(models.Model):
    enName = models.CharField(verbose_name='Name', max_length=200, blank=False)
    color = models.ForeignKey(Color, blank=False)
    shape = models.ForeignKey(Shape, blank=False)
    description = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.enName
