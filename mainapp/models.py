from django.db import models

# Create your models here.
class bad(models.Model):
    who = models.TextField()
    when = models.TextField()
    what = models.TextField()
    why = models.TextField()

class money(models.Model):
    name= models.TextField(null=True)
    total=models.IntegerField()

class cart(models.Model):
    hp= models.TextField(null=True)
    category = models.TextField()
    option = models.TextField(null=True)
    ice = models.TextField()
    cardorSamsung = models.TextField(null=True)




class user(models.Model):
    hp = models.TextField()
    name = models.TextField()

class order(models.Model):
    hp = models.TextField()
    name = models.TextField()
    result = models.BooleanField()
    category = models.TextField()
    reason = models.TextField()