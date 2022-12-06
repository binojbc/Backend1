from django.urls import path,re_path
from . import views


urlpatterns = [
    # path('task/',views.TaskList.as_view()),
    # path('task/<int:pk>/',views.TaskListEdit.as_view()),
    re_path(r'^task/$', views.task_list),
    re_path(r'^task/(?P<pk>[0-9]+)$', views.task_detail),
    
]