from django.forms import ModelForm
from .models import TPegawaiSapk
from django.forms import Form, ChoiceField, CharField

class FormTpegawaiSapk(ModelForm):
    class Meta:
        model = TPegawaiSapk
        fields = '__all__'
