from django.http import HttpResponse
from django.http import JsonResponse
from pages.models import project, Container_Registry


def homePageView(request):
    return HttpResponse("Container resgitry")

def getJson(request):
    obj = project.objects.all()
    data = { "project " :list(obj.values("project_id", "user_id", "role"))}
    return JsonResponse(data)

def getJson_registry(request):
    obj = Container_Registry.objects.all()
    data = { "Container Registry " :list(obj.values("project_id", "registry_name", "create_time", "quota_size"))}
    return JsonResponse(data)

