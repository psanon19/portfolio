from django import forms
from .models import FormModel
from .models import ContactMeModel


class PostForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name', 'address', 'operating_budget', 'description', 'number_of_employees', 'image_url'}
        order_field = {'name', 'address', 'operating_budget', 'description', 'number_of_employees'}


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeModel
        fields = {'name', 'email', 'message',}
        order_field = {'name', 'email', 'message'}