from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feeds(models.model):
    # these fields should function well enough for RSS and Atom.  I still need to look at how podcasts work
    url = models.charfield(max_length=2000)
    version = models.CharField(max_length=5)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    
class article(models.model):
    feed = models.ForiegnKey(Feeds)
    link = models.CharField(max_length=2000)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    viewed = models.BooleanField()
    
class subscriptions(models.model):
    user_id = models.ForiegnKey(User)
    feed_id = models.ForiegnKey(Feeds)
