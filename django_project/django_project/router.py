from pages.viewsets import ProjectViewset, RegistryViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project',ProjectViewset)
router.register('registry', RegistryViewset)
