from django import forms
from .models import UserProfile, Address

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['전화번호', '생일']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['우편번호', '주소', '상세주소']