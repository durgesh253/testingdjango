from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_add, name='book_add'),
    path('books/edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('books/delete/<int:book_id>/', views.book_delete, name='book_delete'),
]
