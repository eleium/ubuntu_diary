from django.contrib import admin

# Register your models here.
from .models import Diary, Entry

admin.site.register(Diary)
admin.site.register(Entry)
