from django import forms
from django.core.validators import ValidationError


class UserForm(forms.Form):
    # def ValidateName(name):
    #
    #     if name.isdigit():
    #
    #         raise ValidationError("Name cannot be complete numeric!")
    #
    #
    # def ValidateEmail(email):
    #
    #     if email.split("@")[1]!= 'mytectra.com':
    #        raise ValidationError("not allowed!")

    cn = (
         ('', '--select option--'),
         ('cn', 'Chennai'),
         ('hyd', 'hyderbad'),
         ('mb', 'mumbai')

    )

    gn = (
         ('m', 'male'),
         ('f', 'female'),
    )
    is_active = forms.CharField(widget=forms.CheckboxInput)
    is_active2 = forms.BooleanField()

    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    City = forms.ChoiceField(choices=cn)

    username = forms.CharField(
        required=True,
        min_length=8,
        max_length=10,
        label='username',
        help_text='username must be 8 characters',
        #initial='Anu',
        error_messages={
            'required': 'username must be atleast 8 charcters'
        },
        # validators=[ValidateName]
    )
    email = forms.EmailField(
        required=True,
        label='email',
        help_text='email must valid ',
        error_messages={
            'reqired': 'email must not blank'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter valid email address'
        }),

        # validators=[ValidateEmail]

    )
    address = forms.CharField(
        widget=forms.Textarea
    )
    password1=forms.CharField()
    password2=forms.CharField()

    # def clean(self):
    #     form_data =self.cleaned_data
    #
    #     if 'username' in form_data:
    #         if form_data['username'].isdigit():
    #             self.errors['username']=['Invalid username!']
    #
    #     if 'email' in form_data:
    #         if form_data['email'].split('@')[1]!=['mytectra.com', 'yahoo.com']:
    #             self.errors['email']=['not allowed!']
    #
    #     if 'password1' in form_data and 'password2' in form_data:
    #         if form_data['password1']!= form_data['password2']:
    #             self.errors['password2']=['password mis match!']
    #
    #     return form_data