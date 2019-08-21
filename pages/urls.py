from django.urls import path
from .views import PagesList_view, PageDetail_view, PageCreate, PageUpdate, PageDelete

urlpatterns = [
    path('', PagesList_view.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/',PageDetail_view.as_view() , name='page'),
    path('created/', PageCreate.as_view(), name = 'page_created'),
    path('update/<int:pk>/', PageUpdate.as_view(), name = 'page_update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name = 'page_delete'),
]