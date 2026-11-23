from django.db import models

# Create your models here.
class F_projects(models.Model): # model for featured projets
    cardTag = models.CharField(max_length=15)
    matSymbol = models.CharField(max_length =50)
    cardTitle = models.CharField(max_length = 40)
    cardDesc = models.CharField(max_length =500)
    avatar = models.CharField(max_length = 5)
    authorName = models.CharField (max_length = 20)
