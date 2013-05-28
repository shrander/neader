from django.db import models

# Create your models here.

class Feeds(models.model):
    url = models.charfield(max_length=500)
    version = models.charfield(max_length=5)
    title = models.charfield(max_length=200)
    description = models.charfield(max_length=500)
    
class article(models.model):
    feed = models.ForiegnKey(Feeds)
    link models.charfield(max_length=500)
    title = models.charfield(max_length=500)
    description = models.charfield(max_length=500)