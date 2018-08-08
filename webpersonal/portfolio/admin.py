from django.contrib import admin
from .models import Project
# Register your models here.
# para extender la configuracion base del administrador herencia
class ProjectAdmin(admin.ModelAdmin):
    #campos solo de lectura
    readonly_fields=('created','updated')




admin.site.register(Project,ProjectAdmin)