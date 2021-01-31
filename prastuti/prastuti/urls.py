"""prastuti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.Home),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
<<<<<<< HEAD
    path('teams/', include('teams.urls'))
=======
    path('event_registration/',include('teams.urls')),
    path('events/',include('events.urls')),
>>>>>>> 879aa97f8e40793251b53c0db2078670804802da
    # path('events/', include('events.urls'))
]
