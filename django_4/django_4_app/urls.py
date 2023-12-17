from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('project_create/', views.ProjectCreate.as_view(), name='project_create'),
    path('project/<int:id>/', views.ProjectView.as_view(), name='project'),
    path('project/edit/<int:id>/', views.project_edit, name='project_edit'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('test/', views.TestView.as_view(), name='test')
]
