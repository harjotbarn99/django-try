from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.

# class CDetailView(View):
#     template_name = "info.html"
#     def get(self,request, *args,**kwargs):
#         return render(request,self.template_name,{})

class CourseDeleteView(View):
    template_name = "courses/deleteCourse.html"

    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course,id=id)
        return obj

    def get(self,request, id=None , *args,**kwargs):
        obj = self.get_object()
        map = {}
        if obj is not None :
            map["object"] = obj
        return render(request,self.template_name,map)

    def post(self,request, *args,**kwargs):
        map= {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect("/courses/")
        return render(request,self.template_name,map)



class CourseUpdateView(View):
    template_name = "courses/updateCourse.html"

    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course,id=id)
        return obj

    def get(self,request, id=None , *args,**kwargs):
        obj = self.get_object()
        map = {}
        if obj is not None :
            form = CourseModelForm(instance=obj)
            map["object"] = obj
            map["form"] = form
        return render(request,self.template_name,map)

    def post(self,request, *args,**kwargs):
        map= {}
        obj = self.get_object()
        map["object"] = obj
        if obj is not None:
            form = CourseModelForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
                map["form"] = form
        return render(request,self.template_name,map)




class CourseCreateView(View):
    template_name = "courses/createCourse.html"

    def get(self,request , *args,**kwargs):
        form = CourseModelForm()
        map={"form" : form}
        return render(request,self.template_name,map)

    def post(self,request, *args,**kwargs):
        form = CourseModelForm(request.POST)
        map={}
        if form.is_valid():
            form.save()
            form = CourseModelForm()
            map={"form" : form}
        return render(request,self.template_name,map)




class CourseListView(View):
    template_name ="courses/mainCourses_view.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self,request, id = None , *args,**kwargs):
        map={"object_list":self.get_queryset()}
        return render(request,self.template_name,map)



class CView(View):
    template_name = "courses/detailCourse.html"

    def get(self,request, id = None , *args,**kwargs):
        map={}
        if id is  not None:
            obj = get_object_or_404(Course, id = id)
            map["object"] = obj
        return render(request,self.template_name,map)

