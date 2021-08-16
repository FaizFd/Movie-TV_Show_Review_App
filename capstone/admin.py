from django.contrib import admin
from .models import User, Listing, Comment, Cart, Alllisting

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Alllisting)