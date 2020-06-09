from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="any label i want",widget=forms.Textarea(attrs={"placeholder": "test placeholder","rows":1,"columns":40}))
    email = forms.EmailField()
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "any twoo three",
                                          "id" : "any_id"
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=10.99)
    class Meta:
        model = Product
        fields =[
            "title",
            "description",
            "price"
        ]

    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "@" in title:
    #         raise forms.ValidationError("Title needs @ in it")
    #     if not ".edu" in title:
    #         raise  forms.ValidationError("no .edu in title")
    #     return title

        def clean_email(self,*args,**kwargs):
            email = self.cleaned_data.get("email")
            if not "@" in email:
                raise forms.ValidationError("Email needs @ in it")
            if not email.endswith(".edu"):
                raise  forms.ValidationError("no .edu in email")
            return email




class RawProdForm(forms.Form):
    # title = forms.CharField()
    # description = forms.CharField()
    # price = forms.DecimalField()


    title = forms.CharField(label="any label i want",widget=forms.Textarea(attrs={"placeholder": "test placeholder","rows":1,"columns":40}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "any twoo three",
                                          "id" : "any_id"
                                      }
                                     )
                                  )
    price = forms.DecimalField(initial=10.99)