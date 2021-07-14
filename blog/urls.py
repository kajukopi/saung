from django.urls import path
# importing views from views..py
from .views import Create,Detail,Delete,Update,List,TentangKami
urlpatterns = [
    path('create', Create, name='blog-create'),
    path('', List, name='blog-list'),
    path('tentangkami', TentangKami, name='blog-tentangkami'),
    path('<id>', Detail, name='blog-detail'),
    path('<id>/delete', Delete, name='blog-delete'),
    path('<id>/update', Update, name='blog-update'),
]
