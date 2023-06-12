from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'updated')


#campos sólo de lectura


admin.site.register(Project, ProjectAdmin)#añadimos la clase anterior