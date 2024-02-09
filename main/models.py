from django.db import models



class Banner(models.Model):
    description = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='banner_photos/')
    title = models.CharField(max_length=75)



class About(models.Model):
    mini_text = models.CharField(max_length=55)



class Service(models.Model):
    description = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='service_photos/')
    title = models.CharField(max_length=55)



class Project(models.Model):
    bio = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='project_photos/')



class Our_Team(models.Model):
    photo = models.ImageField(upload_to='our_team_photos/')
    mini_text = models.CharField(max_length=25)
    instagram = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    facebook = models.CharField(max_length=55)
    google = models.CharField(max_length=55)


class News(models.Model):
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='news_photos/')


