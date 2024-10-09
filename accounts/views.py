from django.shortcuts import render, redirect

# Create your views here.

from .models import User

def index(request): # 마이페이지 같은 , 개인정보 페이지 
    users = User.objects.all() 
    context = {
        'users' : users, 
    }
    return render(request, 'accounts/index.html', context) 







# ---------------------------- login logout -------------------------------

# django 에서 제공하는 login, logout 기능 사용하기 
# (인증된 사용자) 정보를 (세션에 저장) 하는 기능을 분리했다. 

# login 이란, 사용자 정보를 세션에 저장하는 행동. 그걸 가능케 하는 함수 login 
from django.contrib.auth import login as auth_login , logout as auth_logout 

# django 에서 제공하는 유저 유효성 검사(사용자 인증) 기능 활용하기 
from django.contrib.auth.forms import AuthenticationForm # 메서드 get_user() 까지 사용 가능 

# -------------------------------------------------------------------------

def login(request): 
    # 사용자가 만약 이중 로그인을 하려고 url을 통해 login page에 접근한다면 
    if request.user.is_authenticated: 
        return redirect('articles:index')

    # 로그인 폼이 제출되었을 때와 , 그 이전의 행동 정의 
    if request.method == 'POST': 
        form = AuthenticationForm(request, request.POST) 
        if form.is_valid(): 
            auth_login(request, form.get_user())
            # get_user() : 
            # 1. 사용자가 입력한 자격 증명이 데이터베이스의 사용자와 일치하는지 확인 
            # 2. 일치하는 사용자 있으면, 해당 사용자 객체를 반환 
            # from - AuthenticationForm - 
            return redirect('articles:index')
    else: 
        form = AuthenticationForm() 
    context = {
        'form' : form , 
    }
    return render(request, 'accounts/login.html', context) 



# ---------- django 에서 제공하는 @login_required 기능 활용하기 ------------

from django.contrib.auth.decorators import login_required

# -------------------------------------------------------------------------


@login_required 
def logout(request): 
    auth_logout(request) 
    return render(request, 'articles:index')







# ------------------------- signup signout update -------------------------

from . forms import CustomUserChangeForm , CustomUserCreationForm

# -------------------------------------------------------------------------


def signup(request): 
    # 이미 login된 user 가 url 로 접근하는 걸 방지 
    if request.user.is_authenticated: 
        return redirect('articles:index')
    # form 을 login 하는 것도 아니고 , save() 메서드를 사용한다 ? 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request, request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('articles:index') 
    else: 
        form = CustomUserCreationForm() 
    context = {
        'form' : form , 
    }   
    return render(request, 'accounts/signup.html', context) 

@login_required
def signout(request): 
    if request.method == 'POST': 
        request.user.delete() 
        return redirect('articles:index')
    else: 
        return render(request, 'accounts/signout_confirm.html') 

@login_required
def update(request): 
    if request.method == 'POST': 
        form = CustomUserChangeForm(request, request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('articles:index') # 개인정보 수정 화면으로 돌아가야 할 텐데 
    else : 
        form = CustomUserChangeForm() 
    context = {
        'form' : form , 
    }
    return render(request, 'accounts/update.html', context) 






# -------------------------- change_password ------------------------------



# -------------------------------------------------------------------------

@login_required
def change_password(request): 
    pass 