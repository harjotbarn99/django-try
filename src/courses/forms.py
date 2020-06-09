from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    title = forms.CharField(label="Title of Article",widget=forms.Textarea(attrs={"placeholder": " Title","rows":1,"columns":40}))
    avalible = forms.BooleanField()

    class Meta:
        model = Course
        fields =[
            "title",
            "avalible"
        ]