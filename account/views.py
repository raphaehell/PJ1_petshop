from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 홈 페이지로 리다이렉트
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

# 로그인, 로그아웃, 프로필 수정 등 뷰 함수 추가