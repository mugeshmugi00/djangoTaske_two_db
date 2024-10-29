from django.urls import path
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("reg/",views.reg,name="reg"),
    path("home/",views.home,name="home"),
    path("addstudent/",views.addstudent,name="addstudent"),
    path("students/",views.students,name="students"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
    path("cours/", views.cours, name="cours"),
    path("addCours/", views.addCours, name="addCours"),
    path("delete/<str:id>",views.deleteStudent,name="deleteStudent"),
    path("cours/delete/<str:id>",views.deleteCours,name="deleteCours"),
]
