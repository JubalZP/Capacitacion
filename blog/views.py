from django.shortcuts import render

posts = [
    {
        'author': 'Jubal Zúñiga',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'December 9, 2020.'
    },
    {
        'author': 'Corey Taylor',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December 10, 2020.'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
