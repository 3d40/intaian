from django.forms import ModelForm
from .models import TPegawaiSapk


class FormTPegawaiSapk(ModelForm):
	class Meta:
		model = TPegawaiSapk
		fields = '__all__'