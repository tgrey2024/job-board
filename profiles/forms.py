# from django import forms
# from allauth.account.forms import SignupForm

# class CustomSignupForm(SignupForm):
#     USER_TYPE_CHOICES = [
#         ('applicant', 'Applicant'),
#         ('employer', 'Employer'),
#     ]
#     user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

#     def save(self, request):
#         user = super().save(request)
#         user_type = self.cleaned_data['user_type']
#         if user_type == 'applicant':
#             ApplicantProfile.objects.create(applicant=user)
#         elif user_type == 'employer':
#             EmployerProfile.objects.create(employer=user)
#         return user