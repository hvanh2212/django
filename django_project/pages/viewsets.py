from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from . import models
from . import serializers


class ProjectViewset(viewsets.ModelViewSet): 
    queryset = models.project.objects.all()
    serializer_class = serializers.ProjectSerialiser
    def get_queryset(self):              
        return super().get_queryset().filter(user_id=self.request.user.username)

class RegistryViewset(viewsets.ModelViewSet):
    queryset = models.Container_Registry.objects.all()
    serializer_class = serializers.RegistrySerialiser
    permission_classes = (IsAdminUser, )


