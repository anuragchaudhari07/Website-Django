from django import forms
from .models import DivorceComplaint


class DivorceForm(forms.ModelForm):
    class Meta:
        model = DivorceComplaint

        fields = ('o_name','o_email','o_no','o_state','o_city','gender','age','year','get_div','sure_div','court_div','children','c_reln','o_emp','p_emp','c_description','c_document',)

        labels = {
            'o_name': ('Full Name: '), 'o_email': ('Email ID: '), 'o_no': ('Contact No: '), 'o_state': ('State: '), 'o_city': ('City: '), 'gender': ('Your Gender: '), 'age': ('Age: '), 'year': ('Marriage Year: '), 'get_div': ('Who wants to get Divorce: '), 'sure_div': ('How sure are you to get Divorce: '), 'court_div': 'Complaint filed in any court: ', 'children': ('How many children you have? '), 'c_reln': ('Current relation with your partner: '), 'o_emp': ('Are you Employed? '), 'p_emp': ('Is Your partner employed? '), 'c_description': ('Why do you want to get Divorce? '), 'c_document': ('Complaint related documents (for multiple documents upload zip file)'),
        }

        widgets = {
               'gender': forms.RadioSelect(),'get_div': forms.RadioSelect(), 'sure_div': forms.RadioSelect(), 'court_div': forms.RadioSelect(), 'c_reln': forms.RadioSelect(), 'o_emp': forms.RadioSelect(), 'p_emp': forms.RadioSelect(),
               'c_description': forms.Textarea(attrs={'placeholder': 'Enter Brief Description','rows':'5'}),
           }
