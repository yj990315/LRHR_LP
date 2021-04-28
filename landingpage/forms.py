from django import forms

from .models import Estimate

class EstimateForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['purpose_of_estimate','type_of_product']

class TypeOfProductForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['type_of_product']

class PurposeForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['purpose_of_estimate']

class BasicInformationForm(forms.ModelForm):
    
    class Meta:
        model = Estimate
        fields = ['name','phone_number','address']

class AddInformationForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['gender', 'age']

