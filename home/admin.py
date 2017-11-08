from django.contrib import admin
from home.models import Post, Friend

admin.site.register(Friend) # creates a new entry in admin and in the DB MAKEMIGRATIONS and MIGRATE
admin.site.register(Post)
