import os  # 상단에 추가해 주세요 (경로 설정용)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. 보안 설정: 배포 시에는 반드시 False로!
DEBUG = False 

# 2. 허용 호스트: 모든 접속을 허용하거나 Vercel 주소를 넣습니다.
ALLOWED_HOSTS = ['*'] 

INSTALLED_APPS = [
    # DB 기능을 안 쓰면 사실 아래 5개는 지워도 무방하지만, 
    # 기본 관리자 기능을 위해 남겨두셔도 빌드 에러는 안 납니다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

# 3. 데이터베이스: 아예 비워두면 에러가 날 수 있으니 기본값을 유지하되,
# 실제로 파일이 생성되지 않도록 Vercel 환경에서는 무시되게 둡니다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 4. 정적 파일 설정 (Vercel 배포 필수)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # 이 줄을 추가하세요.