from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    msg = models.TextField()
    date =models.DateField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')  # Store images in media folder
    github_link = models.URLField()

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    name = models.CharField(max_length=30)
    progress = models.IntegerField(default=0)
    desc = models.TextField(blank=True,null=True)
    icon = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.name
    