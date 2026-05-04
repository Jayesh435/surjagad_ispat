from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('business/', views.business, name='business'),
    path('products/', views.products, name='products'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('media/', views.media_page, name='media'),
    path('reports/', views.reports, name='reports'),
]
