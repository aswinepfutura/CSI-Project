from django import forms
from django.contrib.auth.forms import UserCreationForm

from data_app.models import Login


class StudentForm(UserCreationForm):

    class Meta:
        model = Login
        fields = ('username', 'name','admission_no','roll_no', 'parent_name','mobile_no','address', 'password1', 'password2')