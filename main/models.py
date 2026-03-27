from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=50)        # 이름
    phone = models.CharField(max_length=20)       # 연락처
    department = models.CharField(max_length=100) # 학과/소속
    motivation = models.TextField()               # 지원동기/각오
    created_at = models.DateTimeField(auto_now_add=True) # 지원 시간

    def __str__(self):
        return self.name
