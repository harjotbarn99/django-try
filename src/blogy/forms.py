from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label="Title of Article",widget=forms.Textarea(attrs={"placeholder": " Title","rows":1,"columns":40}))
    content = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "any twoo three",
                                          "id" : "any_id"
                                      }
                                  )
                                  )
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields =[
            "title",
            "content",
            "active"
        ]