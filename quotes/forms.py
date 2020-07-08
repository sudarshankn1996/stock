from django import forms
from .models import stock

class stockForm(forms.ModelForm):
	class Meta:
		model = stock
		fields = ["ticker"]