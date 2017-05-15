from django.db import models
from django.utils import timezone


class Goods(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    def create(self):
        self.save()

    def delete(self, using=None):
        if models.ForeignKey('auth.Admin')==True :
            self.delete()

    def __str__(self):
        return self.title
