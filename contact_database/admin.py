from django.contrib import admin
from .models import Contact

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Contact, ProjectAdmin)