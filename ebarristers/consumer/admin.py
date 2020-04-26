from django.contrib import admin
from .models import ConsumerComplaint
# Register your models here.

class ConsumerComplaintAdmin(admin.ModelAdmin):

    search_fields = ['o_name','cc_id','new_cid']

    list_filter = ['update_flag','c_filed','p_status']

    list_display = ['o_name','cc_id','update_flag','p_status']

    fieldsets = (
        ('Complainant Information', {
            'fields': ('o_name','o_email','o_no','o_state','o_city')
        }),
        ('Complaint Information', {
            'fields': ('c_title','comp_name','date_dis','comp_no','comp_email','c_description','claim_amt','c_document')
        }),
        ('Payment Information', {
            'fields': ('c_amt', 'p_date', 'p_status', 'new_cid','txn_id')
        }),
        ('Reply to customer', {
            'fields': ('admin_reply','admin_document')
        }),
        ('Update Flag', {
            'fields': ('update_flag',)
        }),
    )

admin.site.register(ConsumerComplaint,ConsumerComplaintAdmin)
