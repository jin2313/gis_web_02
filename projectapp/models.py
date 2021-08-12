from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)  # 폼에 아무것도 적지 않아도 된다는 건 아님 -> 그 옵션은 blank
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)