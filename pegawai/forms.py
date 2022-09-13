from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormTpegawaiSapk(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = '__all__'

class FormTRiwayatJabatan(ModelForm):
    class Meta:
        model = TRiwayatJabatan
        fields = '__all__'

class FormTRiwayatGolongan(ModelForm):
    class Meta:
        model = TRiwayatGolongan
        fields = '__all__'


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')