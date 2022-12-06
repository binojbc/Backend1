from django.urls import path, re_path, include
from userdetailsapp import views



urlpatterns = [
    re_path(r'^user/$', views.user_list),
    re_path(r'^user/(?P<pk>[0-9]+)$', views.user_detail),
    # re_path(r'^login/$', views.loginUser),

]