from django import forms
from form_example.models import Collage

def validationName(name):
    pass
class CollageForm(forms.ModelForm):
    # name = forms.CharField(
    #     min_length=8,
    #     max_length=15,
    # )

    class Meta:
        model = Collage
        # fields = '__all__'
        #OR
        fields = ( 'email', 'address', 'city' )
