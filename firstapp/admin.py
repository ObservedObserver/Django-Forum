from django.contrib import admin

# Register your models here.
from firstapp.models import People,Article,Comment,UserInfo, Ticket

admin.site.register(People)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserInfo)
admin.site.register(Ticket)
