from django.conf.urls import url
import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^register_hander/$', views.register_handle),
    url(r'^register_exist/$',views.register_exist),
    url(r'^login_handle/$', views.login_handle)
]