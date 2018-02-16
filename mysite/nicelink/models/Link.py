import random, string


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LinkManager(models.Manager):
    def create_link(self,oryginal_link_text):
        link = self.create(oryginal_link_text=oryginal_link_text, nice_link_text = self.link_generator())
        return link

    def link_generator( size=6, chars=string.ascii_letters + string.digits):
        text = 'localhost:8000/nicelink/' + ''.join(random.SystemRandom().choice(chars) for _ in range(size))
        print(text)
        return text


class Link(models.Model):
    class Meta:
        app_label = 'nicelink'

    oryginal_link_text = models.URLField(max_length=200)
    nice_link_text = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)

    objects = LinkManager()

    def __str__(self):
        reprezentation = self.oryginal_link_text+ " as " + self.nice_link_text
        return reprezentation

    def link_generator(self,size=6, chars=string.ascii_letters + string.digits):
        self.nice_link_text = ''.join(random.SystemRandom().choice(chars) for _ in range(size))
        return self.nice_link_text

