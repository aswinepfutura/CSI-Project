from django.contrib import messages
from django.shortcuts import render, redirect

from data_app.forms import StudentForm
from data_app.models import Login


# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_home(request):
    return render(request,'admintemp/index.html')

def student_register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            messages.info(request, 'subadmin Registered Successful')
            return redirect('student_view')
    return render(request, 'admintemp/student_register.html', {'form': form})

def student_view(request):
    data = Login.objects.filter(is_student=True)
    return render(request, 'admintemp/student_view.html', {'data': data})