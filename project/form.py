from django import forms
from .models import Diary

class TodoForm(forms.ModelForm):
    text = forms.CharField(label="",widget=forms.Textarea(attrs={
        "class":"form-control",
        "rows":2,
        "cols":120,
        "placeholder": "state ya mind for the day"
    }))
    class Meta:
        model = Diary
        fields = [
            'text'
        ]
    # def __init__(self, *args,**kwargs):
    #     super().__init__(self, *args, **kwargs)
    #     self.fields['text'].widget.attrs.update({'class': "form-control", "placeholder": "state your mind?", "rows": 2,"cols":120})
