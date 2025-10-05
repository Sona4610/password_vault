from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add/', views.add_record, name='addpage'),
    path('display/', views.display_records, name='displayrecords'),
    path('update/<int:id>', views.update_record, name='updatepage'),
    path('delete/<int:id>/', views.delete_record, name='deletepage'),
]
