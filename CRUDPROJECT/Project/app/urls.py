from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (HomePageView, AboutPageView,
       BookListView,BookDetailView,BookCreateView,
          BookUpdateView, BookDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('book/', BookListView.as_view(), name='book'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),

]
