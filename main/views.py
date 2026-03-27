from django.shortcuts import render

def index(request):
    # 이제 POST 요청을 처리하지 않고 페이지만 보여줍니다.
    return render(request, 'index.html')