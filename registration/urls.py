from django.urls import path
from .views import Register_view


urlpatterns = [

    path('signup/', Register_view.as_view(),name = 'signup')

]