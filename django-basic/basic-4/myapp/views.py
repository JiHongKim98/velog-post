from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

import base64

def index(request, name, li_text):
    context = {
        'name' : name,
        'li_text' : li_text
    }
    return render(request, 'myapp_index.html', context)


def POST_index(request):

    # POST
    if request.method == 'POST':
        data = request.POST.get("text_data_input")
        context = {'text_data' : data}

        return render(request, 'post_index.html', context)
    
    # GET
    else:
        context = { }
        
        return render(request, 'post_index.html', context)


def POST_index_cookies(request):
    
    # POST
    if request.method == 'POST':
        data = request.POST.get("text_data_input")
        encoding_data = base64.b64encode(data.encode()).decode()

        # render가 아닌 redirect를 사용하는 이유!
        # 데이터(context)를 템플릿에 보내는것이 아닌
        # 쿠키 데이터가 HTTP 헤더에 포함된 템플릿으로
        # 이동하도록 하기 위함이다!
        # 여기서는 'using_cookies' 라는 URL 패턴 으로 이동
        response = redirect('using_cookies')
        
        # data 변수를 'text_data_cookies' 라는 이름으로
        # Cookie 에 포함
        response.set_cookie('text_data_cookies', encoding_data, max_age=30)

        return response
    
    # GET
    else:
    	# 'text_data_cookies' 라는 쿠키가 있는지 확인
        # 없다면 None 을 반환
        data = request.COOKIES.get('text_data_cookies', None)

        if data:
            decoding_data = base64.b64decode(data).decode()

        else:
            decoding_data = ''

        context = {'text_data' : decoding_data}

        return render(request, 'post_index.html', context)