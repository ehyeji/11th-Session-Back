from django.contrib import admin
from community.models import Posting
from .models import User

# Register your models here.

admin.site.register(Posting)

class UserAdmin(admin.ModelAdmin) : 
    list_display = ('username', 'password')


admin.site.register(User, UserAdmin)
