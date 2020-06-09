from django.urls import path
from .views import CView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = "courses"

urlpatterns=[
    path('',CourseListView.as_view() ,name="allCourses"),
    path('<int:id>/', CView.as_view(),name="particularCourse" ),
    path('create/', CourseCreateView.as_view(), ),
    path('<int:id>/update/', CourseUpdateView.as_view(), ),
    path('<int:id>/delete', CourseDeleteView.as_view(), name="delete" ),

    # path('', abbb,name="testcu" ),

    # path('create2/', product_create_view2, ),
    # path('modify/', modify_data_view, ),
    # path('<int:id>/', dynamic_content_lookup, name="particularProd" ),
    # path('<int:id>/delete', delete_object, name="delete" ),
    # path('all/', queryDisplyAll, name="all" ),
]
