from django.urls import path         # type: ignore
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('',views.index,name="index"),
    path('addrecords/',views.addrecordpage,name="addrecordpage"),
    path('addrecords/addrecorddb',views.addrecorddb,name="addrecorddb"),
    path('displayrecords/',views.displayreccordspage,name="displayrecordspage"),
    path('updatepage/<int:id>/', views.updatepage, name='updatepage'),
    path('updaterecorddb/<int:id>/', views.updaterecorddb, name='updaterecorddb'),
    path('deleterecord/<int:id>/', views.deleterecord, name='deleterecord'), 
] 