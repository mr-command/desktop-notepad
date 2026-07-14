from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myfiles,name="welcome"),
    path('myfiles/',views.myfiles,name="myfile"),
    path('newfile/',views.newfile,name="newfile"),
    path('newfilee/',views.newfile2,name="newfile2"),
    path('notepage/<int:nk>',views.note,name="note"),
]
