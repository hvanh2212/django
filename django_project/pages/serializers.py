from rest_framework import serializers
from pages.models import project, Container_Registry

class ProjectSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = project
        fields = ('project_id', 'user_id', 'role')


class RegistrySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container_Registry
        fields = ('project_id', 'registry_name', 'create_time', 'quota_size')

