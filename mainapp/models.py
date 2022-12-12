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
    category = models.TextField()
    ice = models.TextField()




class user(models.Model):
    hp = models.TextField()
    name = models.TextField()

class order(models.Model):
    hp = models.TextField()
    name = models.TextField()
    result = models.BooleanField()
    category = models.TextField()
    reason = models.TextField()