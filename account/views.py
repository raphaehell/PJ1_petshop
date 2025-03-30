from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import UserProfile, Address
from .forms import UserProfileForm, AddressForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # 회원가입 후 프로필 페이지로 리다이렉트
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # 로그인 후 프로필 페이지로 리다이렉트
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    try:
        address = request.user.address_set.first()  # 사용자의 첫 번째 주소 가져오기
    except Address.DoesNotExist:
        address = Address.objects.create(user=request.user)

    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=user_profile)
        address_form = AddressForm(request.POST, instance=address)
        if user_profile_form.is_valid() and address_form.is_valid():
            user_profile_form.save()
            address_form.save()
            return redirect('profile')  # 프로필 페이지로 리다이렉트
    else:
        user_profile_form = UserProfileForm(instance=user_profile)
        address_form = AddressForm(instance=address)

    return render(request, 'account/profile.html',
                  {'user_profile_form': user_profile_form, 'address_form': address_form})