from django.contrib import admin
from .models import Booktype, Book

admin.site.register(Book)
admin.site.register(Booktype)
