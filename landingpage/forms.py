from django import forms

from .models import Estimate, Photo

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
        fields = ['name','gender','age','phone_number','address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름'}),
            'gender': forms.Select(attrs={'placeholder': '성별'}),
            'age': forms.NumberInput(attrs={'placeholder': '나이'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': '전화번호'}),
            'address': forms.TextInput(attrs={'placeholder':'주소'}),
        }

class AddInformationForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = []

class PhotoForm(forms.ModelForm) :
    class Meta :
        model = Photo
        fields = ['detail_image',]

PhotoFormSet = forms.inlineformset_factory(Estimate, Photo, form=PhotoForm, extra=5)