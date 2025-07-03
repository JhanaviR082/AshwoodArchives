from django.contrib.auth import views as auth_views
from django.urls import path
from .views import piece_detail
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('<int:pk>/', views.details.as_view(), name='details'),
    path('register/', views.UserFormView.as_view(), name="userform"),
    path('login/', auth_views.LoginView.as_view(template_name='genre/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('piece/<int:piece_id>/', views.piece_detail, name='piece_detail'),
]
