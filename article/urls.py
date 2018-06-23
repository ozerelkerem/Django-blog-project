from django.contrib import admin
from django.urls import path

app_name = "article"

from . import views
urlpatterns = [
    path('create/', views.index,name= "create"),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('add/',views.addarticle,name = "add"),
    path('article/<int:id>',views.detail, name = "detail"),
    path('update/<int:id>',views.update,name = "update"),
    path('delete/<int:id>',views.delete,name ="delete"),
    path('comment/<int:id>',views.addcomment,name ="addcomment"),
    path('',views.article,name = "articles"),
]
