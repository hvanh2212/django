from django.contrib import admin
from pages.models import project, Container_Registry

# Register your models here.
@admin.register(project)
class project(admin.ModelAdmin):
    list_projet = ['project_id', 'user_id', 'role']
    admin.register(project)

@admin.register(Container_Registry)
class Container_Registry(admin.ModelAdmin):
    list_registry = ['project_id', 'registry_name', 'create_time', 'quota']
    admin.register(Container_Registry)


