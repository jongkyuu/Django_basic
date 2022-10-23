from urllib import response
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(id=user_id)
        return HttpResponse(f'Welcome {fcuser.username}!')
    else:
        return HttpResponse(f'Home!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not (username and password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        else:
            fcuser  = Fcuser.objects.get(username=username)
            print(f'fcuser.password : {fcuser.password}')
            print(f'password : {password}')
            print(f'check_password result : {check_password(password, fcuser.password)}')
            if check_password(password, fcuser.password):
                # 로그인 처리
                # 세션을 사용한 로그인
                print(f'fcuser.id : {fcuser.id}')
                request.session['user'] = fcuser.id
                # 리다이렉트
                return redirect('/')
                pass
            else:
                res_data['error'] = '비밀번호가 틀렸습니다'


        return render(request, 'login.html', res_data)

def regitster(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
