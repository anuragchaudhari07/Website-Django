from django.contrib import admin
from .models import HarassmentComplaint
# Register your models here.

class HarassmentComplaintAdmin(admin.ModelAdmin):

    search_fields = ['o_name','hc_id','new_cid']

    list_filter = ['update_flag','c_filed','p_status']

    list_display = ['o_name','hc_id','update_flag','p_status']

    fieldsets = (
        ('Complainant Information', {
            'fields': ('o_name','o_email','o_no','o_state','o_city','o_desig')
        }),
        ('Complaint Information', {
            'fields': ('comp_name','comp_email','comp_no','comp_head','comp_state','comp_city','comp_adds','acc_name','acc_desig','relw_acc','icc','c_description','c_document')
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

admin.site.register(HarassmentComplaint,HarassmentComplaintAdmin)
