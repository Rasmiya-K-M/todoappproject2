from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:Tid>/',views.delete,name='delete'),
    path('update/<int:Tid>/',views.update,name='update'),
    path('cblview/',views.LVtask.as_view(),name='cbhome'),
    path('cbdview/<int:pk>/',views.DVtask.as_view(),name='cbid'),
    path('cbupdate/<int:pk>/',views.UVtask.as_view(),name='cbupdate'),
    path('cbdelete/<int:pk>/',views.DelVtask.as_view(),name='cbdelete'),
]
