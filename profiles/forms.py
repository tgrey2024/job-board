from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['firstname', 'lastname', 'role', 'intro', 'address1', 'address2', 'city', 'postcode', 'skills', 'experience', 'profilepic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))