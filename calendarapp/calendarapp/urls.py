
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar_entry/<int:pk>', views.details, name='details'),
    
    #add event path 
    path('entry/add', views.add, name='add'),

    #delete event path
    path('entry/delete/<int:pk>', views.delete, name='delete'),

    # admin path
    path('admin/', admin.site.urls),
]
