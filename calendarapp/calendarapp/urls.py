
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('entry/<int:pk>', views.details, name='details'),
    
    #add event path 
    path('entry/add', views.add, name='add'),

    #delete event path
    path('entry/delete/<int:pk>', views.delete, name='delete'),

    # admin path
    path('admin/', admin.site.urls),

    #login/out paths
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),

    #signup path
    path('signup', views.signup, name='signup'),
]
