from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('skills',views.skills,name='skills'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
