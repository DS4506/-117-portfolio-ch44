from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='static/img')
    respository = models.URLField()
    skill = models.ManyToManyField(Skill)
    
    def __str__(self):
        return f"{self.name} - ({self.year})"
