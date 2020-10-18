from django.contrib import admin

from .models import Screening, Viewer, Genre, Friend, Ticket

admin.site.register(Screening)

admin.site.register(Viewer)

admin.site.register(Genre)

admin.site.register(Friend)

admin.site.register(Ticket)

# Register your models here.
