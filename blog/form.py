from django import forms
from .models import Customer

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields = ('name','phoneNum','reason',)