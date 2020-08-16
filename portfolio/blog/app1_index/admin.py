from django.contrib import admin
from .models import *
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    pass

class Contact_meAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','sent_on',)
    list_filter = ('sent_on',)
    search_fields = ('name',)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill)
admin.site.register(Lang)
admin.site.register(Interests)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Contact_me, Contact_meAdmin)
