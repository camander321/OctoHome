from django.shortcuts import render
from django.http import JsonResponse

# Dummy Data

posts = [
{
    'author': 'bob',
    'title': 'bobs post',
    'content': 'Hey! Im bob',
    'date': 'a long-ass time ago',
},
{
    'author': 'not bob',
    'title': 'not bobs post',
    'content': 'Hey! Im not bob',
    'date': 'a short-ass time ago',
},
]

# Create your views here.

def home(request):
    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)

def help(request):
    return render(request, 'home/help.html')

'''def jsonTest(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)
'''
