from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProdForm
from django.http import Http404


# Create your views here.
#  all objects
def queryDisplyAll(request):
    query = Product.objects.all()
    map = {
        "query_list":query
    }
    return render(request,'product/all_objects.html',map)


#  delete an object
def delete_object(request,id):
    obj = get_object_or_404(Product,id=id)
    if request.method =="POST":
        obj.delete()
        return redirect("/")
    map= {
        "obj" : obj
    }
    return render(request,"product/delete.html",map)



# dynamic content
def dynamic_content_lookup(request,id):
    print(id)
    # obj = Product.objects.get(id=idd)
    # obj = get_object_or_404(Product,id=idd)
    try :
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    map={
        "obj" : obj
    }
    return render(request,"product/dynamic.html",map)

#  modify
def modify_data_view(request):
    obj = Product.objects.get(id=1)
    ini = {
        # "title" : "testing for title",
        "email" : "hh@njs.edu"
    }
    form = ProductForm(request.POST or None, initial=ini, instance=obj)
    if form.is_valid():
        form.save()
    map = {
        "form" : form
    }
    return render(request,"product/modify_view.html",map)


def product_create_view(request,*args,**kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm( )
    map  = {
        "form":form
    }
    return render(request,"product/product_create_view.html",map)

def product_create_view2(request,*args,**kwargs):
    formy = RawProdForm()
    if request.method == "POST":
        formy = RawProdForm(request.POST)
        if formy.is_valid():
            print(formy.data)
            print(formy.cleaned_data)
            Product.objects.create(**formy.cleaned_data)
        else:
            print(formy.errors)
    map  = {
        "formt" : formy
    }
    return render(request,"product/product_create_view2.html",map)


# def product_create_view2(request,*args,**kwargs):
#     print(request.method)
#     print(request.POST)
#     if request.method == "POST":
#         titlePost  = request.POST.get("t")
#         print(titlePost)
#     # Product.objects.create(title = titlePost,price = 0)
#     map  = {
#     }
#     return render(request,"product/product_create_view2.html",map)

def product_details_view(request,*args,**kwargs):
    obj = Product.objects.get(id=1)
    map  = {
        "title" : obj.title,
        "description" : obj.description,
        "price" : obj.price,
        "summary" : obj.summary,
        "featured" : obj.featured
    }
    return render(request,"product/detail.html",map)