from django import forms
from .models import FeedBack
import re
from django.utils.translation import gettext_lazy as _

class FeedBackForm(forms.ModelForm):

    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'col-12 btn-outline border border-info rounded btn-lg', 'placeholder': "Ваш телефон"}), required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'col-12 border border-info rounded btn-lg', 'placeholder': "Ваше имя"}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'col-12 border border-info rounded btn-lg', 'placeholder': "Ваша почта"}), required=True)
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'style': 'resize:none;height:128px;',
                'class': "col-12 px-1 mx-0 form-control align-top border border-info rounded btn-lg",
                'placeholder': "Введите ваше сообщение"
                }
            ), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = _('Номер телефона')
        self.fields['name'].label = _('Имя')
        self.fields['email'].label = _('Электронная почта')
        self.fields['text'].label = _('Сообщение')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['com', 'net']:
            raise forms.ValidationError(
                f'Регистрация для домена {domain} невозможна'
            )
        return email

    class Meta:
        model = FeedBack
        fields = ['phone', 'name', 'email', 'text']

        

    
