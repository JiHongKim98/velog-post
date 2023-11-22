from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

# kimDB 모델
from .models import kimDB
# htmlForm 폼
from .forms import htmlForm


def using_DB_test(request):

    # request.POST 의 반환 값은?!
    # ex) <QueryDict: {'csrfmiddlewaretoken': ['<csrf_token_value>'], 'hidden': ['<data_id_value>'], 'form_del_DB': ['삭제']}>
    # 예시에서 hidden 의 데이터를 꺼내쓸려면?!
    # ex) request.POST.get('hidden')
    
    # POST 방식
    if request.method == 'POST':

        # POST 된 form name : "form_save" 즉, 저장
        if 'form_save' in request.POST:

            # form 값 가져오기
            form = htmlForm(request.POST)

            # form 유효성 검사 '.is_valid'
            if form.is_valid():
                form.save()
                return redirect('using_DB')
        
    
    # GET 방식
    else:
        # form 생성
        form = htmlForm()
    
        # order_by('필드명') '-필드명' : 내림차순, '필드명' : 오름차순
        context_DB = kimDB.objects.all().order_by('-id')

        context = {
            'form':form, 'context_DB': context_DB
            }

        return render(request, 'index_test.html', context)