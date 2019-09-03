from django.urls import path
from .views import HiloView, HiloDetailView

urlpatterns = [

    path('',HiloView.as_view(),name='thread_list'),
    path('thread/<int:pk>',HiloDetailView.as_view(),name = 'thread_detail'),

]