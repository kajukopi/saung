from django.urls import path
# importing views from views..py
from .views import (Create,
                    Detail,
                    Delete,
                    Update,
                    List,
                    About,
                    User_Login,
                    User_Logout,
                    User_Register,
                    )
urlpatterns = [
    path('create', Create, name='blog-create'),
    path('', List, name='blog-list'),
    path('about', About, name='blog-about'),
    path('<id>', Detail, name='blog-detail'),
    path('<id>/delete', Delete, name='blog-delete'),
    path('<id>/update', Update, name='blog-update'),
    path("register", User_Register, name='blog-register'),
    path("login", User_Login, name='blog-login'),
    path("logout", User_Logout, name='blog-logout'),
]
