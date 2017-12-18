from django.db import models

# Create your models here.


class Blog(models.Model):
    btitle = models.CharField(max_length=20)
    bname = models.CharField(max_length=20)
    bcount = models.IntegerField(default=0)



class Content(models.Model):
    ctitle = models.ForeignKey(Blog)
    cname = models.CharField(max_length=20)
    cinfo = models.CharField(max_length=200)



# -------------------------------------------------

class Author(models.Model):
    aname = models.CharField(max_length=15)
    aage = models.IntegerField(default=18)
    asex = models.BooleanField(default=0)

class Eassy(models.Model):
    etitle = models.CharField(max_length=10)
    etext = models.CharField(max_length=50)
    ecount = models.IntegerField(default=0)
    eauthor = models.ForeignKey(Author)




