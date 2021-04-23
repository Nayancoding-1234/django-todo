from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta():
        model = Todo
        fields = ['task','due_date']
        widgets = {
            'task':forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Enter your task"} ),
            'due_date':forms.DateInput(attrs={"class":"form-control" ,"placeholder":"DD/MM/YYYY"} )
        }



   
