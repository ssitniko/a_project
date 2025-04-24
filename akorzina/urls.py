from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about_us/', views.about_us_view, name='about_us'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('payment_delivery/', views.payment_delivery_view, name='payment_delivery'),
    path('catalog/chandeliers/', views.chandeliers_view, name='chandeliers'),
    path('catalog/lampshades/', views.lampshades_view, name='lampshades'),
    path('catalog/mirrors/', views.mirrors_view, name='mirrors'),
    path('catalog/pano/', views.pano_view, name='pano'),
    path('catalog/other/', views.other_view, name='other'),


]