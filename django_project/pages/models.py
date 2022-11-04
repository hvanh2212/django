from django.db import models

# Create your models here.
class project(models.Model):
    project_id = models.CharField(null = False, blank = False, max_length=512)
    user_id = models.CharField(null = False, blank = False, max_length=512)
    role = models.CharField(null = False, blank = False, max_length=512)
    class Meta:
        managed = False
        unique_together = ('project_id','user_id')
    @classmethod
    def create(cls, _project_id, _user_id, _role):
        record = cls(project_id = _project_id, user_id = _user_id, role= _role)
        return record

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Container_Registry(models.Model):
    project_id = models.CharField(null = False, blank = False, max_length=512)
    registry_name = models.CharField(null = False, blank = False, primary_key=True, max_length=512)
    create_time = models.CharField(null = False, blank = False, max_length=512)
    quota_size = models.IntegerField(null = False, blank = False)
  
    @classmethod
    def create(cls, _project_id, _registry_name, _create_time, _quota_size):
        record = cls(project_id = _project_id, registry_name = _registry_name, create_time= _create_time, quota_size = _quota_size)
        return record

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
