
from django import forms
from todoapp.models import Posts

class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"