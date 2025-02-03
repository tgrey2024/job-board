from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Apply'))