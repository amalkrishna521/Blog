from django.contrib import admin
from .models  import post ,category,profile,Comment

# Register your models here.
admin.site.register(post)
admin.site.register(category)
admin.site.register(profile)
admin.site.register(Comment)