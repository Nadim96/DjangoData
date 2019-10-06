"""AtosProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import views

app_name = 'orders'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit_order/(?P<pk>[0-9]+)/$', views.EditOrder, name='edit_order'),
    url(r'^add_order/$', views.AddOrderForm, name='add_order'),
    url(r'^delete_order/(?P<pk>[0-9]+)/$', views.DeleteOrder, name='delete_order'),
    url(r'^edit_order_form/(?P<pk>[0-9]+)/$', views.EditOrderForm, name='edit_order_form'),
    url(r'^upload_csv/$', views.UploadCsv, name='upload_csv')
]
