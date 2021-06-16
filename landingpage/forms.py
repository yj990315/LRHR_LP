from django import forms

from .models import Estimate


class EstimateForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['purpose_of_estimate','type_of_product']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['brand', 'price', 'year']
        widgets = {
            'brand': forms.TextInput(),
            'price': forms.TextInput(attrs={'placeholder':'정가가 아닌 구입 가격을 적어주세요.'}),
            'year': forms.TextInput(),
        }
        labels = {
            'brand': '브랜드',
            'price': '구입 가격',
            'year': '구입 년도',
        }

class BasicInformationForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ['name','phone_number','address']
        widgets = {
            'name': forms.TextInput(),
            'phone_number': forms.NumberInput(attrs={'placeholder': '예) 01012345678'}),
            'address': forms.TextInput(),
        }
        labels = {
            'name': '이름',
            'phone_number': '전화번호',
            'address': '주소',
        }
        def __init__(self, *args, **kwargs):
         self.fields['age'].error_messages = {'max_length': '올바른 나이를 입력했는지 확인해주세요.'}
