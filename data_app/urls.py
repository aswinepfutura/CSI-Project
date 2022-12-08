from django.urls import path

from data_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('student_register',views.student_register,name='student_register'),
    path('student_view',views.student_view,name='student_view'),
]