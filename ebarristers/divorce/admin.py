from django.contrib import admin
from .models import DivorceComplaint
# Register your models here.

class DivorceComplaintAdmin(admin.ModelAdmin):

    search_fields = ['o_name','dc_id','new_cid']

    list_filter = ['update_flag','c_filed','p_status']

    list_display = ['o_name','dc_id','update_flag','p_status']

    fieldsets = (
        ('Complainant Information', {
            'fields': ('o_name','o_email','o_no','o_state','o_city','gender','age')
        }),
        ('Complaint Information', {
            'fields': ('year','get_div','sure_div','court_div','children','c_reln','o_emp','p_emp','c_description','c_document')
        }),
        ('Payment Information', {
            'fields': ('c_amt', 'p_date', 'p_status','new_cid','txn_id')
        }),
        ('Reply to customer', {
            'fields': ('admin_reply','admin_document')
        }),
        ('Update Flag', {
            'fields': ('update_flag',)
        }),
    )

admin.site.register(DivorceComplaint,DivorceComplaintAdmin)
