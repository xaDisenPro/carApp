from django import forms
from django.core.exceptions import ValidationError

from user.models import UserProfile


class RegistForm(forms.ModelForm):
    passwd2 = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        fields = '__all__'

        error_messages = {
            'name': {
                'required': '用户名不能为空',
            },
            'email': {
                'required': '邮箱不能为空',
            },
            'passwd': {
                'required': '口令不能为空'
            },
            'passwd2': {
                'required': '重复口令不能为空'
            }
        }

    def clean_passwd2(self):
        passwd1 = self.cleaned_data.get('passwd')
        passwd2 = self.cleaned_data.get('passwd2')
        if passwd1 != passwd2:
            raise ValidationError('两次口令不相同')

        return passwd1


class LoginForm(forms.Form):
    name = forms.CharField(label='用户名',
                           min_length=10,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           error_messages={
                               'required': '用户名不能为空',
                               'min_length': '用户名不能少于10个字符'
                           })

    password = forms.CharField(label='口令',
                               min_length=10,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={
                                   'required': '口令不能为空',
                                   'min_length': '口令不能少于10个字符'
                               }
                               )
