"""hbsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hbsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hbsApp.urls")),
    path('user/index',views.index),
    path('user/login',views.login_call, name="login_call"),
    path('user/register',views.register, name="register"),
    path('user/bookHistory',views.bookHistory),
    path('user/HotelList', views.hotelList),
    path('user/logout',views.logout_call, name="logout_call"),
    path("user/destinations_filtered.json", views.json_view)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

