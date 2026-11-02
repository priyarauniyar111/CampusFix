from django.conf import settings
from django.db import models
import uuid
class Complaint(models.Model):
 CATEGORIES=[('Hostel','Hostel'),('Classroom','Classroom'),('Electricity','Electricity'),('Wi-Fi','Wi-Fi'),('Cleanliness','Cleanliness'),('Water','Water'),('Other','Other')]
 PRIORITIES=[('Low','Low'),('Normal','Normal'),('Urgent','Urgent')]
 STATUSES=[('Submitted','Submitted'),('Under Review','Under Review'),('In Progress','In Progress'),('Resolved','Resolved'),('Rejected','Rejected')]
 ticket_id=models.CharField(max_length=12,unique=True,editable=False)
 student=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='complaints')
 title=models.CharField(max_length=120);category=models.CharField(max_length=24,choices=CATEGORIES)
 location=models.CharField(max_length=120);description=models.TextField()
 priority=models.CharField(max_length=12,choices=PRIORITIES,default='Normal')
 image=models.ImageField(upload_to='complaints/%Y/%m/',blank=True,null=True)
 status=models.CharField(max_length=20,choices=STATUSES,default='Submitted')
 department=models.CharField(max_length=80,blank=True);admin_note=models.TextField(blank=True)
 created_at=models.DateTimeField(auto_now_add=True);updated_at=models.DateTimeField(auto_now=True)
 def save(self,*args,**kwargs):
  if not self.ticket_id:self.ticket_id=uuid.uuid4().hex[:8].upper()
  super().save(*args,**kwargs)
 def __str__(self):return f'{self.ticket_id} · {self.title}'
 class Meta:ordering=['-created_at']
