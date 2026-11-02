from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='home'),path('signup/',views.signup,name='signup'),path('login/',views.login_view,name='login'),path('logout/',views.logout_view,name='logout'),path('dashboard/',views.dashboard,name='dashboard'),path('complaints/new/',views.create_complaint,name='create_complaint'),path('complaints/<str:ticket_id>/',views.complaint_detail,name='complaint_detail'),path('complaints/<str:ticket_id>/update/',views.update_complaint,name='update_complaint')]
