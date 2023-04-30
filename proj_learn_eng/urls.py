"""proj_learn_eng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('vocabulary', views.vocabulary),
    path('lessons-list', views.lessons_list),
    path('terms-list/<slug:slug>/', views.terms_list_new),
    path('add-word', views.add_word),
    path('send-word', views.send_word),
    path('send-lesson', views.send_lesson),
    path('send-del-word', views.send_del_word),
    path('stats', views.show_stats),
    path('add-lesson', views.add_lesson)

]
