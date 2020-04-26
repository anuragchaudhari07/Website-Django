from django.db import models
import datetime
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core.validators import MinLengthValidator

# Create your models here.

GENDER_CHOICES = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHER','OTHER')
)

ICC_CHOICES = (
    ('YES','YES'),
    ('NO','NO'),
)

AGE_CHOICES = (
    ('20-25','20-25'),
    ('26-35','26-35'),
    ('36-45','36-45'),
    ('46-55','46-55'),
    ('56+','56+'),

)

YEAR_CHOICES = []
for r in range(1940, (datetime.datetime.now().year) + 1):
    YEAR_CHOICES.append((r,r))

GET_DIV = (
    ('YOU','YOU'),
    ('YOUR PARTNER','YOUR PARTNER'),
)

SURE_DIV = (
    ('I AM NOT SURE','I AM NOT SURE'),
    ('I AM SURE, BUT NEED GUIDANCE','I AM SURE, BUT NEED GUIDANCE')
)

CHILDREN_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5+','5+'),
)

RELATION_CHOICES = (
    ('LOW CONFLICT','LOW CONFLICT'),
    ('HIGH CONFLICT','HIGH CONFLICT'),
    ('SUSPICIOUS','SUSPICIOUS'),
)

class DivorceComplaint(models.Model):

    dc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name='Complainant Name')  #pk

    # own info of customer
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    o_name = models.CharField(max_length=128,verbose_name='Complainant Name')  #complainant name
    o_email = models.EmailField(max_length=64,verbose_name='Complainant Email')  #complainant email
    o_no = PhoneNumberField(verbose_name='Complainant No')  #complainant no
    o_state = models.CharField(max_length=32,verbose_name='Complainant Name')  #complainant state
    o_city = models.CharField(max_length=32,verbose_name='Complainant City')  #complainant city

    gender = models.CharField(max_length=8,choices=GENDER_CHOICES,default='MALE',verbose_name='Gender')  #complainant gender
    age = models.CharField(max_length=8,choices=AGE_CHOICES,default='20-25',verbose_name='Complainant Age')  #complainant age
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year,verbose_name='Year of Marriage')  #year of marriage
    get_div = models.CharField(max_length=16,choices=GET_DIV,default='YOU',verbose_name='Who wants Divorce') #who wants divorce
    sure_div = models.CharField(max_length=64,choices=SURE_DIV,default='I AM NOT SURE',verbose_name='How sure you are to get divorce') #how sure to get divorce
    court_div = models.CharField(max_length=3,choices=ICC_CHOICES,default='YES',verbose_name='Divorce filed at court')  #divorce filed in court
    children = models.CharField(max_length=2,choices=CHILDREN_CHOICES,default='1',verbose_name='No. of children')  #no of children
    c_reln = models.CharField(max_length=16,choices=RELATION_CHOICES,default='LOW CONFLICT',verbose_name='Current relation status')  #current relation
    o_emp = models.CharField(max_length=4,choices=ICC_CHOICES,default='YES',verbose_name='Complainant employed')  #own employability
    p_emp = models.CharField(max_length=4,choices=ICC_CHOICES,default='YES',verbose_name='Partner employed')  #partner employability
    c_description = models.TextField(max_length=4056,verbose_name='Complainant Description',validators=[MinLengthValidator(30)])  #complaint discription
    c_document = models.FileField(upload_to='divorce/',null=True,blank=True,verbose_name='Complaint related documents')
    c_filed = models.DateField(auto_now_add=True,verbose_name='Complaint filed date')

    c_amt = models.DecimalField(decimal_places=2,max_digits=1000000000,verbose_name='Complaint Amount',null=True,blank=True)
    p_date = models.DateTimeField(null=True,verbose_name='Payment Date',blank=True)
    p_status = models.BooleanField(verbose_name='Payment Status',default=0)
    new_cid = models.CharField(max_length=128,null=True,blank=True,verbose_name='Order ID')
    txn_id = models.CharField(max_length=128,null=True,blank=True,verbose_name='Transaction ID')

    update_flag = models.BooleanField(verbose_name='Information Updated',default=0)

    admin_reply = models.TextField(max_length=4056, verbose_name='Update Complaint Status',null=True,blank=True)
    admin_document = models.FileField(upload_to='admin/divorce/',null=True,blank=True,verbose_name='Attach documents')

    def __str__(self):
        return self.o_name
