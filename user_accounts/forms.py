from django import forms
from .models import UserProfile, Address

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    introduction = forms.CharField(max_length=200, required=False) # 소개 필드 추가

    class Meta:
        model = UserProfile
        fields = ['profile_picture', '전화번호', '생일', 'introduction'] # 소개 필드 추가

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['우편번호', '주소', '상세주소']