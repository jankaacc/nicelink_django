from django.db import models


from .Link import Link


class UserModel(models.Model):
    class Meta:
        app_label = 'nicelink'

    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique= True)
    fullname = models.CharField(max_length=40)
    # links = models.ForeignKey(Link, on_delete=models.CASCADE)

    def __str__(self):
        return '<Username: %r>' %self.username
