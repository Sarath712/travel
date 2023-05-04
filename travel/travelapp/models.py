from django.db import models

class Place(models.Model):
    objects = None
    default = "No Description"
    name = models.CharField(max_length=250, null=True)
    img = models.ImageField(upload_to='pics', null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name

class seven(models.Model):
    objects = None
    default = "No Description"
    name = models.CharField(max_length=250, null=True)
    img = models.ImageField(upload_to='pics', null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name