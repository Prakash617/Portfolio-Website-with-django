from django.db import models

# Create your models here.

class Myteam(models.Model):
    img  = models.ImageField(upload_to = 'My_team')
    name = models.CharField(max_length=75, null=False, blank= False)
    profession = models.CharField(max_length=75, null=False, blank= False)
    

    def __str__(self):
        return self.name
    
class AboutMe(models.Model):
    img  = models.ImageField(upload_to = 'About_me')
    desc = models.CharField(max_length=1000, null=False, blank= False)


    def __str__(self):
        return self.desc[:10]