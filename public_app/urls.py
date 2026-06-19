from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]