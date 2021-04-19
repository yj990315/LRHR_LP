from django import forms

from .models import Estimate

class EstimateForm(forms.ModelForm):

    class Meta:
        model = Estimate
        fields = ('purpose_of_estimate','type_of_product','brand',)
