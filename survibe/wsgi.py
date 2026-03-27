import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'survibe.settings')

application = get_wsgi_application()

# 이 한 줄이 반드시 맨 아래에 있어야 합니다! (오타 주의: 소문자 app)
app = application