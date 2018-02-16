from django.contrib import admin


from .models.User import UserModel
from .models.Link import Link
# Register your models here.

admin.site.register(Link)
admin.site.register(UserModel)
