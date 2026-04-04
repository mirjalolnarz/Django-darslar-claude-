from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def bosh_sahifa(request):
    context = {
        'sarlavha': 'Xush kelibsiz, bu mening blogim!',
        'postlar': [
            {'id': 1, 'title': 'Birinchi post', 'muallif': 'Ali'},
            {'id': 2, 'title': 'Ikkinchi post', 'muallif': 'Vali'},
            {'id': 3, 'title': 'Uchinchi post', 'muallif': 'Hasan'},
        ]
    }

    return render(request, 'posts/bosh.html', context)

def haqida(request):
    return render(request, 'posts/haqida.html')

def post_detail(request, post_id):
    context = {
        'sarlavha': f'Post {post_id} tafsilotlari',
        'post': {
            'id': post_id,
            'title': f'Post {post_id} sarlavhasi',
            'content': f'Bu yerda Post {post_id} ning tafsilotlari ko\'rsatiladi.',
            'muallif': 'Ali',
        }
    }
    return render(request, 'posts/detail.html', context)

def foydalanuvchi(request, username):
    return HttpResponse(f"<h1>Foydalanuvchi: {username}</h1> <p>Bu yerda foydalanuvchining profili ko'rsatiladi.</p>")

def maqola(request, slug):
    return HttpResponse(f"<h1>Maqola: {slug}</h1> <p>Bu yerda maqolaning tafsilotlari ko'rsatiladi.</p>")