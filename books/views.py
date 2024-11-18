from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.http import HttpResponse
from .models import Book, UserLogin

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        
        if UserLogin.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            UserLogin.objects.create(name=name, email=email, password=password)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserLogin.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid password.')
        except UserLogin.DoesNotExist:
            messages.error(request, 'Email not registered.')
    
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    user_name = request.session.get('user_name')
    return render(request, 'dashboard.html', {'user_name': user_name})


# List books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'dashboard/book_list.html', {'books': books})

# Add a new book
def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')
        pages = request.POST.get('pages')
        available = request.POST.get('available') == 'on'

        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            pages=pages,
            available=available
        )
        messages.success(request, 'Book added successfully!')
        return redirect('book_list')
    
    return render(request, 'dashboard/book_form.html')

# Edit an existing book
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.isbn = request.POST.get('isbn')
        book.pages = request.POST.get('pages')
        book.available = request.POST.get('available') == 'on'
        book.save()

        messages.success(request, 'Book updated successfully!')
        return redirect('book_list')
    
    return render(request, 'dashboard/book_form.html', {'book': book})

# Delete a book
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book_list')