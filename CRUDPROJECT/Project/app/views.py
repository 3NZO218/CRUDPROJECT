from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

from django.db.models import Sum, Count

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'app/book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.get_queryset()
        
        context['search_query'] = self.request.GET.get('q', '')
        context['total_books'] = books.count()
        context['sum_book_price'] = books.aggregate(Sum('price'))['price__sum'] or 0
        context['total_authors'] = books.annotate(num_authors=Count('author')).aggregate(Count('author', distinct=True))['author__count']
        context['total_publishers'] = books.aggregate(Count('publisher', distinct=True))['publisher__count']
        context['total_users'] = books.aggregate(Count('user', distinct=True))['user__count']
        
        return context

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'app/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'app/book_create.html'



class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'app/book_update.html'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'app/book_delete.html'
    success_url = reverse_lazy('book')