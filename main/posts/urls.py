from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<slug>/', views.DetailView.as_view(), name='post_detail'),
]