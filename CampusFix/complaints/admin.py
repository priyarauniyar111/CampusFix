from django.contrib import admin
from .models import Complaint
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
 list_display=('ticket_id','title','student','category','priority','status','department','created_at')
 list_filter=('status','category','priority','department');search_fields=('ticket_id','title','student__username','location')
 list_editable=('status','department');readonly_fields=('ticket_id','created_at','updated_at')
