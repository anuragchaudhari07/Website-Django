from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ConsumerComplaint

class DateInput(forms.DateInput):
	input_type = 'date'

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = ConsumerComplaint

        fields = ('o_name','o_email','o_no','o_state','o_city','c_title','comp_name','date_dis','comp_no','comp_email','c_description','claim_amt','c_document')

        labels = {
            'o_name': ('Full Name: '), 'o_email': ('Email ID: '), 'o_no': ('Contact No: '), 'o_state': ('State: '), 'o_city': ('City: '), 'c_title': ('Complaint Title: '), 'comp_name': ('Company Name: '), 'date_dis': ('Date of Dispute: '),  'comp_no': ('Company Contact No: '), 'comp_email': ('Company Email: '), 'c_description': ('Complaint Description: '), 'claim_amt': ('Approximate Claim Amount: '),
			'c_document': ('Complaint related documents (for multiple documents upload zip file)')
        }

        widgets = {
               'date_dis': DateInput(),'c_title': forms.TextInput(attrs={'placeholder': 'Enter Your Complaint is About'}),
			   'c_description': forms.Textarea(attrs={'placeholder': 'Enter Brief Description','rows':'5'}),
			   # 'claim_amt': forms.DecimalField(attrs={'placeholder': 'INR'}),

           }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password1',
        'password2',
        ]
        help_texts = {k:"" for k in fields}
