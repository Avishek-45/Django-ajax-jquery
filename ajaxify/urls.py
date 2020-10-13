from django.urls import path
from ajaxify import views

urlpatterns = [
    path('contact/',views.contact,name='contact')
]
