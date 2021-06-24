from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('delete/<str:article>', views.delete, name='delete an article'),
    path('userChangeInformations/', views.userChangeInformations, name="Change user's information"),
]