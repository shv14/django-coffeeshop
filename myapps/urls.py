from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    # path('admin', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]