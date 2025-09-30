from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname')


# admin.site.register(Member) # type: ignore
admin.site.register(Member, MemberAdmin)

# Register your models here.
