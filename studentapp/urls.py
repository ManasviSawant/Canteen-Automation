"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name='home'),
    path("studlogin", views.studlogin, name='studlogin'),
    path("studregister", views.studregister, name='studregister'),
    path("logout", views.logout, name='logout'),
    path("studindex", views.studindex, name='studindex'),
    path("menu", views.menu, name='menu'),
    path("addtocart", views.addtocart, name='addtocart'),
    path("removecartdata", views.removecartdata, name='removecartdata'),
    path("cartdata", views.cartdata, name='cartdata'),
    path("checkout", views.checkout, name='checkout'),
    path("placeorder", views.placeorder, name='placeorder'),
    path("invoicehistory", views.invoicehistory, name='invoicehistory'),
    path("userfeedback", views.userfeedback, name='userfeedback'),
    path("sendotp", views.sendotp, name='sendotp'),
    path("setpassword", views.setpassword, name='setpassword'),







] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
