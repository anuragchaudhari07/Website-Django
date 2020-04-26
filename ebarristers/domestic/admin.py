from django.contrib import admin
from .models import DomesticComplaint
# Register your models here.

class DomesticComplaintAdmin(admin.ModelAdmin):

    search_fields = ['o_name','doc_id','new_cid']

    list_filter = ['update_flag','c_filed','p_status']

    list_display = ['o_name','doc_id','update_flag','p_status']

    fieldsets = (
        ('Complainant Information', {
            'fields': ('o_name','o_email','o_no','o_state','o_city','o_adds','gender')
        }),
        ('Complaint Information', {
            'fields': ('acc_name','acc_email','acc_no','acc_state','acc_city','acc_adds','acc_gender','case_pending_a','case_pending_w','c_description','c_document')
        }),
        ('Payment Information', {
            'fields': ('c_amt', 'p_date', 'p_status', 'new_cid', 'txn_id')
        }),
        ('Reply to customer', {
            'fields': ('admin_reply','admin_document')
        }),
        ('Update Flag', {
            'fields': ('update_flag',)
        }),
    )

admin.site.register(DomesticComplaint,DomesticComplaintAdmin)
