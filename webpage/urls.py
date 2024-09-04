from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name='contact'),
    path("card/", views.card, name='card'),
    path("cardcolor/", views.cardcolor, name='cardcolor'),
    path("form/", views.form, name='form'),
    path("forpage/", views.forpage, name='forpage'),
]