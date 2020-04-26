from django.db import models
from django import forms
import datetime
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.utils import timezone
# Create your models here.


def present_or_past_date(value):
    if value > datetime.date.today():
        raise forms.ValidationError("The date cannot be in the future!")
    return value

class ConsumerComplaint(models.Model):

    cc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name='Complaint ID')  #pk

    # own info of customer
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    o_name = models.CharField(max_length=128,verbose_name='Complainant Name')  #complainant name
    o_email = models.EmailField(max_length=64,verbose_name='Complainant Email')  #complainant email
    o_no = PhoneNumberField(verbose_name='Complainant No')  #complainant no
    o_state = models.CharField(max_length=32,verbose_name='Complainant Name')  #complainant state
    o_city = models.CharField(max_length=32,verbose_name='Complainant City')  #complainant city

    c_title = models.CharField(max_length=128,null=True,verbose_name='Complainant Title')  #complaint tiltle
    comp_name = models.CharField(max_length=128,verbose_name='Company Name')  #company name
    date_dis = models.DateField(verbose_name='Date of Dispute',validators=[present_or_past_date])  #date of dispute
    comp_no = PhoneNumberField(blank=True,null=True,verbose_name='Company contact No')  #company number
    comp_email = models.EmailField(blank=True,null=True,verbose_name='Company Email')  #company email
    c_description = models.TextField(max_length=4056,verbose_name='Complainant Description',validators=[MinLengthValidator(30)])  #complaint discription
    claim_amt = models.DecimalField(decimal_places=2,max_digits=1000000000,verbose_name='Claim Amount')  #claim amount
    c_document = models.FileField(upload_to='consumer/',null=True,blank=True,verbose_name='Complaint related documents')
    c_filed = models.DateField(auto_now_add=True,verbose_name='Complaint filed date')#correction

    c_amt = models.DecimalField(decimal_places=2,max_digits=1000000000,verbose_name='Complaint Amount',null=True,blank=True)
    p_date = models.DateTimeField(null=True,verbose_name='Payment Date',blank=True)
    p_status = models.BooleanField(verbose_name='Payment Status',default=0)
    new_cid = models.CharField(max_length=128,null=True,blank=True,verbose_name='Order ID')
    txn_id = models.CharField(max_length=128,null=True,blank=True,verbose_name='Transaction ID')

    update_flag = models.BooleanField(verbose_name='Information Updated',default=0)

    admin_reply = models.TextField(max_length=4056, verbose_name='Update Complaint Status',null=True,blank=True)
    admin_document = models.FileField(upload_to='admin/consumer/',null=True,blank=True,verbose_name='Attach documents')

    def __str__(self):
        return self.o_name
