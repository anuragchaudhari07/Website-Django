from django.db import models
import datetime
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.validators import MinLengthValidator
# Create your models here.

ICC_CHOICES = (
    ('YES','YES'),
    ('NO','NO'),
)


class HarassmentComplaint(models.Model):

    hc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name='Complainant Name')  #pk

    # own info of customer
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    o_name = models.CharField(max_length=128,verbose_name='Complainant Name')  #complainant name
    o_email = models.EmailField(max_length=64,verbose_name='Complainant Email')  #complainant email
    o_no = PhoneNumberField(verbose_name='Complainant No')  #complainant no
    o_state = models.CharField(max_length=32,verbose_name='Complainant Name')  #complainant state
    o_city = models.CharField(max_length=32,verbose_name='Complainant City')  #complainant city

    o_desig = models.CharField(max_length=32,verbose_name='Complainant Designation')  #complainant designation
    comp_name = models.CharField(max_length=128,verbose_name='Company Name')  #company name
    comp_no = PhoneNumberField(blank=True,null=True,verbose_name='Company contact No')  #company number
    comp_email = models.EmailField(blank=True,null=True,verbose_name='Company Email')  #company email
    comp_head = models.CharField(max_length=128,verbose_name='Company Head')  #company head
    comp_state = models.CharField(max_length=32,verbose_name='Company State')  #company state
    comp_city = models.CharField(max_length=32,verbose_name='Company City')  #company city
    comp_adds = models.TextField(max_length=256,blank=True,null=True,verbose_name='Company Address')  #company address
    acc_name = models.CharField(max_length=128,verbose_name='Accused Name')  #accused name
    acc_desig = models.CharField(max_length=32,verbose_name='Accused Designation')  #accused designation
    relw_acc = models.CharField(max_length=32,verbose_name='Working Relation with Accused')  #working relation with accused
    icc = models.CharField(max_length=4,choices=ICC_CHOICES,default='YES',verbose_name='Complaint filed at ICC') #is complain filed at ICC
    c_description = models.TextField(max_length=4056,verbose_name='Complainant Description',validators=[MinLengthValidator(30)])  #complaint discription
    c_document = models.FileField(upload_to='harassment/',null=True,blank=True,verbose_name='Complaint related documents')
    c_filed = models.DateField(auto_now_add=True,verbose_name='Complaint filed date')

    c_amt = models.DecimalField(decimal_places=2,max_digits=10,verbose_name='Complaint Amount',null=True,blank=True)
    p_date = models.DateTimeField(null=True,verbose_name='Payment Date',blank=True)
    p_status = models.BooleanField(verbose_name='Payment Status',default=0)
    new_cid = models.CharField(max_length=128,null=True,blank=True,verbose_name='Order ID')
    txn_id = models.CharField(max_length=128,null=True,blank=True,verbose_name='Transaction ID')

    update_flag = models.BooleanField(verbose_name='Information Updated',default=0)

    admin_reply = models.TextField(max_length=4056, verbose_name='Update Complaint Status',null=True,blank=True)
    admin_document = models.FileField(upload_to='admin/harassment',null=True,blank=True,verbose_name='Attach documents')

    def __str__(self):
        return self.o_name
