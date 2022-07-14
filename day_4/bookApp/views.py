from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Category, Author
# Create your views here.
def index(request):
    books = Book.objects.all()
    #for book in books:
    #    print(book.title, book.author.name,book.category.last_name)
    #print(books)
    return render (request, 'bookApp/index.html', {
        "books_list":books
    })
    #return HttpResponse("app-book")

def author (request, author_id):
    return HttpResponse("author id : "+author_id)

def Category (request, category_id):
    return HttpResponse("category id:"+category_id)
