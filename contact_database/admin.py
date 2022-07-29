from django.contrib import admin
from .models import Contact

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('name','updated','email','message')
    search_fields=('name','updated','created','email','phone','age','sex','comunication','reason','message')
    list_filter=('updated',)
    date_hierarchy='updated'   
    

admin.site.register(Contact, ProjectAdmin)