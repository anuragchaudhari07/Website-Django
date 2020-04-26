from django import forms
from .models import DomesticComplaint

class DomesticForm(forms.ModelForm):
    class Meta:
        model = DomesticComplaint

        fields = ('o_name', 'o_adds','o_state','o_city','o_email','o_no', 'gender','acc_name','acc_adds','acc_state','acc_city','acc_email','acc_no','acc_gender','case_pending_a','case_pending_w', 'c_description','c_document',)

        labels = {
            'o_name': ('Full Name: '), 'o_email': ('Email ID: '), 'o_no': ('Contact No: '), 'o_state': ('State: '), 'o_city': ('City: '), 'o_adds': ('Address: '), 'gender': ('Gender: '), 'acc_name': ('Full Name: '), 'acc_email': ('Email ID: '), 'acc_no': ('Contact No: '), 'acc_state': ('State: '), 'acc_city': ('City: '), 'acc_adds': ('Address: '), 'acc_gender': ('Gender: '), 'case_pending_a': ('Is your case pending before any court? '), 'case_pending_w': ('Is your case pending before any State Commission for Women? '), 'c_description': ('Brief Description: '), 'c_document': ('Complaint related documents (for multiple documents upload zip file)')
        }

        widgets = {
               'gender': forms.RadioSelect(), 'acc_gender': forms.RadioSelect(), 'case_pending_a': forms.RadioSelect(), 'case_pending_w': forms.RadioSelect(),
               'c_description': forms.Textarea(attrs={'placeholder': 'Enter Brief Description','rows':'5'}),
               'o_adds': forms.Textarea(attrs={'placeholder': 'Enter Address','rows':'5'}),
               'acc_adds': forms.Textarea(attrs={'placeholder': 'Enter address','rows':'5'}),

        }
