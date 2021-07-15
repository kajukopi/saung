from django.urls import path
# importing views from views..py
from .views import (Create,
                    Detail,
                    Delete,
                    Update,
                    List,
                    About,
                    register_request,
                    login_request,
                    logout_request,
                    )



urlpatterns = [
    path('create', Create, name='blog-create'),
    path('', List, name='blog-list'),
    path('about', About, name='blog-about'),
    path('<int:pk>', Detail, name='blog-detail'),
    path('<int:pk>/delete', Delete, name='blog-delete'),
    path('<int:pk>/update', Update, name='blog-update'),
    path('register', register_request , name='blog-register'),
    path('login', login_request, name='blog-login'),
    path('logout', logout_request, name= 'blog-logout'),

]
