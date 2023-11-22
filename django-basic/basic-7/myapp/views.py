from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

# 객체를 가져오기 위해 사용하는 라이브러리
# 객체가 존재하지 않는다면 404 오류를 띄운다!
# 여기서는 'kimDB' 라는 객체 즉, DB 를 가져오기 위해 사용했다
from django.shortcuts import get_object_or_404
# kimDB 모델
from .models import kimDB
# htmlForm 폼
from .forms import htmlForm


def using_DB_index(request):

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
            

        # POST 된 form name : "form_edit_save" 즉, 수정완료 (DB에 upload)
        elif 'form_edit_save' in request.POST:

            # 수정할 데이터를 DB 에서 가져오기
            # get_object_or_404('가져올 DB NAME', pk='수정할 DB의 id')
            edit_data = get_object_or_404(kimDB, pk=request.POST.get('hidden'))

            # DB에 업로드
            form = htmlForm(request.POST, instance = edit_data)
            if form.is_valid():
                form.save()
                return redirect('using_DB')
            
        
        # POST 된 form name : "form_edit" 즉, 수정시작
        elif 'form_edit' in request.POST:

            get_POST_DB_ID = request.POST.get('hidden')
            get_kimDB = kimDB.objects.get(id = get_POST_DB_ID)

            get_POST_up = request.POST.get('up')

            if get_POST_up == '':
                context_DB = kimDB.objects.all()

            else:
                # order_by('필드명') '-필드명' : 내림차순, '필드명' : 오름차순
                context_DB = kimDB.objects.all().order_by('-id')
            
            # 수정을 원하는 데이터를 'kimDB'에서 가져와서
            # form 변수에 저장!
            form = htmlForm(initial = {
                'text_fields' : get_kimDB.text_fields, 'bool_fields' : get_kimDB.bool_fields,
                'char_fields': get_kimDB.char_fields
                })

            context = {
                'form' : form, 'data_before_edit' : get_kimDB, 'edit_type' : True, 'edit_ID' : get_POST_DB_ID
            }

            return render(request, 'index_DB.html', context)
        

        # POST 된 form name : "form_del_DB" 즉, DB에서 삭제
        elif 'form_del_DB' in request.POST:
            
            # 삭제할 데이터를 DB 에서 가져오기
            # get_object_or_404('가져올 DB NAME', pk='삭제할 DB의 id')
            # 객체가 존재하지 않는다면 404 오류를 띄운다
            edit_data = get_object_or_404(kimDB, pk=request.POST.get('hidden'))

            # DB에서 삭제
            edit_data.delete()
            return redirect('using_DB')


    # GET 방식
    else:
        # form 생성
        form = htmlForm()
    
        context_DB = kimDB.objects.all().order_by('-id')

        context = {
            'form':form, 'context_DB': context_DB, 'edit_type' : False
            }

        return render(request, 'index_DB.html', context)