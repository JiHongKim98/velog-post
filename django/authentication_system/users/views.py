from django.shortcuts import render, redirect

# django 내장 모듈 authenticate, login, logout
# authenticate 함수는 클라이언트로 부터 입력받은 ID와 PASSWORD를 통해서 
# 사용자 정보가 저장된 DB 내에서 해당하는 객체가 있는지 검사하고, 
# 올바른 경우 해당 사용자 객체를 반환하고, 올바르지 않은경우에는 NONE을 반환한다.

# login 함수는 user 를 로그인 상태로 만들어준다. 즉, authenticate 함수를 통해서 
# DB 내에서 반환받은 객체를 받아와서 현제 session 데이터 내에 로그인 데이터를 저장한다. 
# 또, 'request.user' 를 사용해서 현재 로그인된 사용자 정보를 가져올 수 있게 해준다.

# logout 함수는 session cookie 에서 클라이언트의 로그인 정보를 삭제해준다.
from django.contrib.auth import authenticate, login, logout
from .models import UserDB


def login_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')

        if account == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticate 검사 (사용자 인증) => return 'None' or USERS object in 'userDB'
            userObject = authenticate(username = username, password = password)

            # is Not None (login success)
            if userObject is not None:

                # request & user object 를 django 내장 모듈
                # login 의 인자로 사용하여 로그인 가능하게 해줄수 있다.
                # template 에서 {{ user.is_authenticated }} 으로
                # 로그인된 사용자 데이터를 알 수 있다.
                login(request, userObject)

            
            # is None (login fail)
            else:
                print('fail')

        # account = 'join' (회원가입)
        else:
            return redirect('users:JoinUrl')

    else:
        pass

    return render(request, 'login.html', { })


def logout_index(request):
    logout(request)
    return redirect('users:LoginUrl')


def join_index(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        print(account)

        if account == 'create':
            new_username = request.POST.get('username')
            new_password = request.POST.get('password')
            new_password_check = request.POST.get('password_check')
            print(new_username)
            print(new_password)

            # 예외처리 1 (ID or PASSWORD 가 완성되지 않음)
            if not new_username or not new_password:
                return render(request, 'join.html', {'error_msg' : '아이디 또는 비밀번호를 입력하세요.'})
            
            # 예외처리 2 (PASSWORD 확인에서의 error)
            elif new_password != new_password_check:
                return render(request, 'join.html', {'error_msg':'비밀번호가 서로 같지 않습니다.'})
            
            # 예외처리 3 (ID 중복)
            elif UserDB.objects.filter(username=new_username).exists():
                return render(request, 'join.html', {'error_msg':'이미 사용중인 아이디입니다.'})
            
            # no exception (이상 없음)
            new_users = UserDB.objects.create_user(username=new_username, password=new_password)
            new_users.save()
            
        
        # account == 'cancel'
        else:
            pass

        return redirect('users:LoginUrl')

    return render(request, 'join.html', {})