from django import forms
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Re-Enter Email:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        all_clean_date = super().clean()

        email = all_clean_date['email']
        vmail = all_clean_date['verify_email']

        if email!=vmail :
            raise forms.ValidationError('Make sure Emails do match')


        



