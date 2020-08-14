from django.forms import ModelForm, TextInput, Textarea
from .models import Customer


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'phone', 'Message')
		widgets = {
			'name': TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
			'phone': TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
			'Message': Textarea(attrs={'class': 'form-control', 'rows':'8','placeholder':'Message'})
		}
