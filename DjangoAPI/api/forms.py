from django import forms
from .models import Features

class FeatureForm(forms.ModelForm):
    class Meta:
              model = Features
              fields = "__all__"

    age = forms.FloatField()
    installmentSize = forms.FloatField()
    installment_1 = forms.FloatField()
    installment_2 = forms.FloatField()
    installment_3 = forms.FloatField()
    installment_4 = forms.FloatField()
    installment_5 = forms.FloatField()
    installment_6 = forms.FloatField()
    installment_7 = forms.FloatField()
    installment_8 = forms.FloatField()
    installment_9 = forms.FloatField()
    installment_10 = forms.FloatField()
    installment_11 = forms.FloatField()


    #
    # gender = forms.TypedChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    # age = forms.IntegerField()
    # salary = forms.IntegerField()