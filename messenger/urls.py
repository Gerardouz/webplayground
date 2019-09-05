from django.urls import path
from .views import HiloView, HiloDetailView, add_mensaje,start_message

urlpatterns = [

    path('',HiloView.as_view(),name='thread_list'),
    path('thread/<int:pk>',HiloDetailView.as_view(),name = 'thread_detail'),
    path('thread/<int:pk>/add', add_mensaje , name = 'add_mensaje'),
    path('thread/start/<username>/', start_message , name = 'start'),
]