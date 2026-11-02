from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from .forms import SignUpForm,ComplaintForm
from .models import Complaint
def home(request):
 if request.user.is_authenticated:return redirect('dashboard')
 return render(request,'home.html')
def signup(request):
 if request.method=='POST':
  form=SignUpForm(request.POST)
  if form.is_valid():
   user=form.save();login(request,user);messages.success(request,'Welcome to CampusFix. Your account is ready!');return redirect('dashboard')
 else:form=SignUpForm()
 return render(request,'auth.html',{'form':form,'heading':'Create your account','subheading':'Join your campus community','mode':'signup'})
def login_view(request):
 if request.method=='POST':
  form=AuthenticationForm(request,data=request.POST)
  if form.is_valid():login(request,form.get_user());return redirect('dashboard')
  messages.error(request,'Check your username and password and try again.')
 else:form=AuthenticationForm(request)
 return render(request,'auth.html',{'form':form,'heading':'Welcome back','subheading':'Sign in to track your campus requests','mode':'login'})
def logout_view(request):
 logout(request);return redirect('home')
@login_required
def dashboard(request):
 qs=Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(student=request.user)
 query=request.GET.get('q','').strip();status=request.GET.get('status','')
 if query:qs=qs.filter(Q(title__icontains=query)|Q(ticket_id__icontains=query)|Q(location__icontains=query))
 if status:qs=qs.filter(status=status)
 all_qs=Complaint.objects.all() if request.user.is_staff else Complaint.objects.filter(student=request.user)
 counts={'total':all_qs.count(),'active':all_qs.exclude(status__in=['Resolved','Rejected']).count(),'resolved':all_qs.filter(status='Resolved').count()}
 return render(request,'dashboard.html',{'complaints':qs,'counts':counts,'query':query,'selected_status':status,'statuses':Complaint.STATUSES})
@login_required
def create_complaint(request):
 if request.method=='POST':
  form=ComplaintForm(request.POST,request.FILES)
  if form.is_valid():
   complaint=form.save(commit=False);complaint.student=request.user;complaint.save();messages.success(request,f'Complaint submitted! Your tracking ID is {complaint.ticket_id}.');return redirect('complaint_detail',ticket_id=complaint.ticket_id)
 else:form=ComplaintForm()
 return render(request,'complaint_form.html',{'form':form})
def can_manage(user):return user.is_staff or user.is_superuser
@login_required
def complaint_detail(request,ticket_id):
 complaint=get_object_or_404(Complaint,ticket_id=ticket_id)
 if not (request.user.is_staff or complaint.student_id==request.user.id):return redirect('dashboard')
 return render(request,'detail.html',{'complaint':complaint})
@login_required
@user_passes_test(can_manage)
def update_complaint(request,ticket_id):
 complaint=get_object_or_404(Complaint,ticket_id=ticket_id)
 if request.method=='POST':
  status=request.POST.get('status','')
  if status in dict(Complaint.STATUSES):complaint.status=status
  complaint.department=request.POST.get('department','').strip();complaint.admin_note=request.POST.get('admin_note','').strip();complaint.save();messages.success(request,'Complaint updated successfully.')
 return redirect('complaint_detail',ticket_id=ticket_id)
