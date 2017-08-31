from django.shortcuts import render
from django.views import generic

from catalog.models import Book, BookInstance, Author


def index(request):
    """
    View function for home page of site.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(request,
                  'index.html',
                  context={
                      'num_books': num_books,
                      'num_instances': num_instances,
                      'num_instances_available': num_instances_available,
                      'num_authors': num_authors
                      },
                  )


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='war')[:5]
    template_name = 'books/my_arbitrary_template_name_list.html'


class BookDetailView(generic.DeleteView):
    model = Book
