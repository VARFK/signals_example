from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import caches
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from book_shelf.models import Book, User
from book_shelf.forms import BookForm, LoginForm, BookReviewForm


def index(request):
    user = None
    if 'user' in request.session:
        user = User.objects.get(pk=request.session['user'])
    context = {}
    context['book_list'] = get_books()
    if user:
        context['username'] = user.name
        context['privileges'] = user.privileges
        context['user_books'] = user.books_lent.all()
    return render(request, 'index.html', context)


def login(request):
    state = "Please log in below..."
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.instance
            return redirect('index')
        else:
            state = "Your username and/or password were incorrect."
    return render(request, 'login.html', {'state': state,
                                          'form': LoginForm()})


def logout(request):
    del request.session['user']
    return redirect('index')


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'book_edit.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('index')
    return render(request, 'book_delete.html', {'object': book})


def book_lend(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        user = User.objects.get(pk=request.session['user'])
        user = book_lend_logic(user, book)
        return redirect('index')
    except Exception as e:
        return render(request, '404.html', {'error': e.message})


def book_return(request, pk):
    try:
        user = User.objects.get(pk=equest.session['user'])
        book = user.books_lent.get(pk=pk)
        user = book_return_logic(user, book)
        return redirect('index')
    except Exception as e:
        return render(request, '404.html', {'error': e.message})


def get_books():
    return Book.objects.all()


def book_lend_logic(user, book):
    if user:
        if user.books_lent.filter(id=book.id).exists():
            raise Exception("The book is already in the user's list")
        book.num_copies = book.num_copies - 1
        book.save()
        user.books_lent.add(book)
        user.save()
        return user
    else:
        raise Exception("User is not available")


def book_return_logic(user, book):
    if user:
        book.num_copies = book.num_copies + 1
        book.save()
        user.books_lent.remove(book)
        user.save()
        return user
    else:
        raise Exception("User is not available")


def book_review(request, pk):
    user = get_object_or_404(User, pk=request.session['user'])
    book = get_object_or_404(Book, pk=pk)
    form = BookReviewForm(request.POST or None,
                          initial={'book': book, 'user': user})
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'book_review.html', {'form': form})
