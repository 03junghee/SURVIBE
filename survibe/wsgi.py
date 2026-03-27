import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'survibe.settings')

application = get_wsgi_application()

# Vercel이 이 application을 인식할 수 있게 'app'으로 별칭 지정
app = application