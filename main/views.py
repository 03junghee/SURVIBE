from django.shortcuts import render
from .mongodb import save_application  # 우리가 만든 함수 가져오기
from datetime import datetime

def index(request):
    if request.method == "POST":
        # 사용자가 입력한 데이터 '날것' 그대로 가져오기
        data = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'department': request.POST.get('department'),
            'motivation': request.POST.get('motivation'),
            'created_at': datetime.now() # 신청 시간 추가
        }

        # 몽고디비에 바로 저장 (에러 날 일이 없음!)
        try:
            save_application(data)
            return render(request, 'success.html')
        except Exception as e:
            print(f"DB 저장 에러: {e}")
            return render(request, 'index.html', {'error': '신청 중 오류가 발생했습니다.'})

    return render(request, 'index.html')