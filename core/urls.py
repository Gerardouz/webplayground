from django.urls import path
from .views import HomePage_View, SamplePage_view

urlpatterns = [
    path('', HomePage_View.as_view(), name="home"),
    path('sample/', SamplePage_view.as_view(), name="sample"),
]
