from django import forms
from .models import Consultation


class UserForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('customer', 'phone')
        labels = {
            'customer': '',
            'phone': ''
        }
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'consultation__form_input',
                                               'placeholder': "Введите Имя"}),
            'phone': forms.TextInput(attrs={'class': 'consultation__form_input',
                                            'placeholder': "+ 7 (999) 000 00 00"}),
        }


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ('customer', 'phone')
        labels = {
            'customer': '',
            'phone': ''
        }
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'order__form_input',
                                               'placeholder': "Введите Имя"}),
            'phone': forms.TextInput(attrs={'class': 'order__form_input',
                                            'placeholder': "+ 7 (999) 000 00 00"}),
        }

