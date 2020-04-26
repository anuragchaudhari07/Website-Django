from django import forms
from .models import HarassmentComplaint

class HarassmentForm(forms.ModelForm):
    class Meta:
        model = HarassmentComplaint

        fields = ('o_name', 'o_desig', 'o_email','o_no','o_state','o_city','comp_name', 'comp_no', 'comp_email', 'comp_head', 'comp_state', 'comp_city', 'comp_adds', 'acc_name', 'acc_desig', 'relw_acc', 'icc', 'c_description','c_document',)

        labels = {
            'o_name': ('Full Name: '), 'o_desig': ('Designation: '), 'o_email': ('Email ID: '), 'o_no': ('Contact No: '), 'o_state': ('State: '), 'o_city': ('City: '), 'comp_name': ('Name: '), 'comp_no': ('Contact No: '), 'comp_email': ('Email: '), 'comp_head': ('Head of the Organisation or (Contact Person): '), 'comp_state': ('State: '), 'comp_city': ('City: '), 'comp_adds': ('Address: '), 'acc_name': ('Name(s) of Accused: '), 'acc_desig': ('Designation(s) of Accused'), 'relw_acc': ('Working Relationship(s) with Accused'), 'icc': ('Have you registered your complaint with ICC: '), 'c_description': ('Brief Description: '), 'c_document': ('Complaint related documents (for multiple documents upload zip file)'),
        }

        widgets = {
               'icc': forms.RadioSelect(),
               'c_description': forms.Textarea(attrs={'placeholder': 'Enter Brief Description','rows':'5'}),
               'comp_adds': forms.Textarea(attrs={'placeholder': 'Enter address','rows':'5'}),
               'comp_name': forms.TextInput(attrs={'placeholder': 'Enter Organisation Name'}),
           }
