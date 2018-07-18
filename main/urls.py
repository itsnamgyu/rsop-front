from django.urls import path, include
from main import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('rsop2018', views.index, name='rsop'),
    path('rsop2018/projects/<int:pk>', views.project, name='rsop-projects'),
    path('rsop2018/projects/feedback/<int:pk>', views.project_feedback, name='rsop-project-feedback'),
]
